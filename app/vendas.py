import pymysql
from app import app
from config import mysql, auth
from flask import jsonify, Response, flash, request
from flask_debug import Debug
from mysql.connector import Error
from flask_basicauth import BasicAuth
import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# clientes = os.environ['ENDPOINT_CLIENTES']    #'http://clientes_api:5100'
# cursos = os.environ['ENDPOINT_PRODUTOS']      #'http://produtos_api:5300'

# clientes = '127.0.0.1:5100'
# cursos = '127.0.0.1:5300'

clientes = os.environ['clientes_rota']
cursos = os.environ['cursos_rota']

basic_auth = auth


# Adicionando um registro
# Não é necessário passar o ID da compra, pois é AI, POST
@app.route('/vendas', methods=['POST'])
@basic_auth.required
def add_compra():
    try:
        _json = request.get_json(force=True)
        _data = _json['data']
        _idCliente = _json['idCliente']
        _idCurso = _json['idCurso']

        if _data and _idCliente and _idCurso and request.method == 'POST':
            sqlQuery = "INSERT INTO db_vendas.tbl_cliente_compra_cursos (data, idCliente, idCurso ) VALUES (%s,%s,%s)"
            bindData = (_data, _idCliente, _idCurso)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)

            # Verificação se o Id do cliente confere com o db_clientes
            cliente = requests.get(f'http://{clientes}/clientes/{_idCliente}', headers={
                                   "Authorization": "Basic c2lsc2lsOjEyMzQ1Njc="})
            curso = requests.get(f'http://{cursos}/produtos/{_idCurso}', headers={
                                 "Authorization": "Basic c2lsc2lsOjEyMzQ1Njc="})
            #status = requests.get(f'http://127.0.0.1:5200/cursos/status/{_idCurso}', headers = {"Authorization":"Basic c2lsc2lsOjEyMzQ1Njc="})

            # Verificando se o cliente e o curso existem:
            if cliente.status_code == 404:
                return ('Cliente não encontrado.'), 404
            elif curso.status_code == 404:
                return ('Curso não encontrado.'), 404
            # Verificando se o Curso possui Status Ativo = 'S'
            status = curso.json()['ativo']
            if status == 'N':
                return ('Produto indisponível, compra não cadastrada!'), 404
            elif status == 'S':
                cursor.execute(sqlQuery, bindData)
                conn.commit()
                response = jsonify('Compra adicionada com sucesso!')
                response.status_code = 200
                return response
        else:
            return not_found()
    except Exception as error:
        return f'{error}', 500
    finally:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.close()
        conn.close()


# Criando as Rotas API para relação JOIN Cliente, Compra e Produtos/Cursos
# Buscando todas as vendas cadastradas (GET)
@app.route('/vendas', methods=['GET'])
# @basic_auth.required
def compras():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            'SELECT idCompra, idCliente, idCurso, DATE_FORMAT(data,"%Y-%m-%d") as data FROM db_vendas.tbl_cliente_compra_cursos')
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as error:
        return jsonify({"error": f"{error}"}), 500
    finally:
        cursor.close()
        conn.close()


# Buscando todas as vendas cadastradas por id de clientes (GET)
# http://127.0.0.1:5000/clientes/compras/id
@app.route('/vendas/<int:idCliente>', methods=['GET'])
@basic_auth.required
def id_compras(idCliente):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            'SELECT idCompra, data, idCliente, idCurso FROM db_vendas.tbl_cliente_compra_cursos WHERE idCliente = %s', idCliente)
        userRow = cursor.fetchall()
        if not userRow:
            return Response('Compra não cadastrada', status=404)

        # Buscando os dados dos clientes e do curso que constam no inventário (userRow) - JOIN
        #cliente = requests.get(f'http://127.0.0.1:5000/clientes/{idCliente}', headers = {"Authorization":"Basic c2lsc2lsOjEyMzQ1Njc="})
        curso = []  # lista de json dos vários cursos comprados por um cliente
        cliente = requests.get(f'http://{clientes}/clientes/{idCliente}', headers={
                               "Authorization": "Basic c2lsc2lsOjEyMzQ1Njc="})
        for i in (userRow):
            #j = i['idCurso']
            #c = requests.get(f'http://127.0.0.1:5200/cursos/{j}', headers = {"Authorization":"Basic c2lsc2lsOjEyMzQ1Njc="})
            #c = requests.get('http://127.0.0.1:5200/cursos/{}'.format(i['idCurso']), headers = {"Authorization":"Basic c2lsc2lsOjEyMzQ1Njc="})
            # c = requests.get(f'{cursos}/cursos/{i["idCurso"]}', headers = {"Authorization":"Basic c2lsc2lsOjEyMzQ1Njc="})
            # i["data"] = f"{i['data']}"
            # curso.append(c.json())
            c = requests.get(f'http://{cursos}/produtos/{i["idCurso"]}', headers={
                             "Authorization": "Basic c2lsc2lsOjEyMzQ1Njc="}, verify=False)
            i["data"] = f"{i['data']}"
            curso.append(c.json())

        # Imprimindo resultado
        response = jsonify(userRow, cliente.json(), curso)
        response.status_code = 200
        return response
    except Exception as error:
        return jsonify({"error": f"{error}"}), 500
    finally:
        cursor.close()
        conn.close()

# Alterando algum curso (PUT)
# No put, precisa passar o ID na rota, mas no próprio body eu posso manter o mesmo, ou colocar o número novo a ser alterado.
@app.route('/vendas/<int:id>', methods=['PUT'])
@basic_auth.required
def update_curso(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _json = request.get_json(force=True)
        _idCompra = _json['idCompra']
        _data = _json['data']
        _idCliente = _json['idCliente']
        _idCurso = _json['idCurso']

        if _data and _idCliente and _idCurso and _idCompra and request.method == 'PUT':
            sqlQuery = "SELECT * FROM db_vendas.tbl_cliente_compra_cursos WHERE idCompra=%s"
            cursor.execute(sqlQuery, id)
            select = cursor.fetchone()
            if not select:
                return Response('Compra não cadastrada', status=400)
            sqlQuery = "UPDATE tbl_cliente_compra_cursos SET data=%s, idCliente=%s, idCurso=%s, idCompra=%s WHERE idCompra=%s"
            bindData = (_data, _idCliente, _idCurso, _idCompra, id)
            # Verificação se o Id do cliente confere com o db_clientes
            cliente = requests.get(f'http://{clientes}/clientes/{_idCliente}', headers={
                                   "Authorization": "Basic c2lsc2lsOjEyMzQ1Njc="})
            curso = requests.get(f'http://{cursos}/produtos/{_idCurso}', headers={
                                 "Authorization": "Basic c2lsc2lsOjEyMzQ1Njc="})

            if cliente.status_code == 404:
                return ('Cliente não encontrado'), 400
            elif curso.status_code == 404:
                return ('Curso não encontrado'), 400
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Dados alterados com sucesso!')
            response.status_code = 200
            return response
        else:
            return not_found()
    except Exception as error:
        return jsonify({"error": f"{error}"}), 500
    finally:
        cursor.close()
        conn.close()


# Deletando algum curso (DELETE)
@app.route('/vendas/<int:idCompra>', methods=['DELETE'])
@basic_auth.required
def delete_curso(idCompra):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlQuery = "SELECT * FROM db_vendas.tbl_cliente_compra_cursos WHERE db_vendas.tbl_cliente_compra_cursos.idCompra=%s"
        cursor.execute(sqlQuery, idCompra)
        select = cursor.fetchone()
        if not select:
            return Response('Compra não cadastrada', status=400)
        cursor.execute(
            "DELETE FROM db_vendas.tbl_cliente_compra_cursos WHERE idCompra =%s", (idCompra))
        conn.commit()
        respone = jsonify('Compra deletada com sucesso!')
        respone.status_code = 200
        return respone
    except Exception as error:
        return jsonify({"error": f"{error}"}), 500
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5400)
