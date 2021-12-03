import pymysql
from app import app
from config import mysql, auth
from flask import Flask, jsonify, Response, request
from flask_debug import Debug
from flask_basicauth import BasicAuth

basic_auth = auth

# API - Clientes

# Adicionando um registro de cliente - POST
@app.route('/clientes', methods=['POST'])
@basic_auth.required
def add_user():
    try:
        _json = request.get_json(force=True)
        _nome = _json['nome']
        _cpf = _json['cpf']
        _email = _json['email']
        _telefone = _json['telefone']
        _senha = _json['senha']

        if _nome and _cpf and _email and _telefone and _senha and request.method == 'POST':
            sqlQuery = "INSERT INTO db_clientes.tbl_clientes (nome, cpf, email, telefone, senha) VALUES (%s,%s,%s,%s,%s)"
            bindData = (_nome, _cpf, _email, _telefone, _senha)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Cliente adicionado com sucesso!')
            response.status_code = 200
            return response
        else:
            return not_found()
    except Exception as error:
        print(error)
    finally:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.close()
        conn.close()

# Retornando todos os registros de clientes - GET
@app.route('/clientes', methods=['GET'])
@basic_auth.required
def get_user():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        print(request)
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT id, nome, cpf, email, telefone, senha FROM db_clientes.tbl_clientes")
        userRows = cursor.fetchall()
        response = jsonify(userRows)
        response.status_code == 200
        return response

    except Exception as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

# Realiza o login do cliente - POST
@app.route('/clientes/login', methods=['POST'])
@basic_auth.required
def login_user():
    try:
        _json = request.get_json(force=True)
        _email = _json['email']
        _senha = _json['senha']

        if _email and _senha and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(
                "SELECT * FROM db_clientes.tbl_clientes WHERE email=%s and senha=%s", (_email, _senha))
            userRow = cursor.fetchone()
            if not userRow:
                return Response('Login inválido', status=400)
            response = jsonify('Login válido!')
            response.status_code = 200
            return response
        else:
            return not_found()
    except Exception as error:
        print(error)
    finally:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.close()
        conn.close()

# Retornando o registro de cliente de um ID específico - GET.
@app.route('/clientes/<int:id>',  methods=['GET'])
@basic_auth.required
def id_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT id, nome, cpf, email, telefone, senha FROM db_clientes.tbl_clientes WHERE id=%s", id)
        userRow = cursor.fetchone()
        if not userRow:
            return Response('Usuário não cadastrado', status=404)
        response = jsonify(userRow)
        response.status_code == 200
        return response
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

# Alterando algum registro de cliente - PUT
@app.route('/clientes', methods=['PUT'])
@basic_auth.required
def update_user():
    try:
        _json = request.get_json(force=True)
        _id = _json['id']
        _nome = _json['nome']
        _cpf = _json['cpf']
        _email = _json['email']
        _telefone = _json['telefone']
        _senha = _json['senha']
        if _nome and _cpf and _email and _telefone and _senha and _id and request.method == 'PUT':
            sqlQuery = "UPDATE db_clientes.tbl_clientes SET nome=%s, cpf=%s, email=%s, telefone=%s, senha=%s WHERE id=%s"
            bindData = (_nome, _cpf, _email, _telefone, _senha, _id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Dados alterados com sucesso!')
            response.status_code = 200
            return response
        else:
            return not_found()
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

# Deletando algum registro de cliente - DELETE
@app.route('/clientes/<int:id>', methods=['DELETE'])
@basic_auth.required
def delete_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlQuery = "SELECT * FROM db_clientes.tbl_clientes WHERE id=%s"
        cursor.execute(sqlQuery, id)
        select = cursor.fetchone()
        if not select:
            return Response('Cliente não cadastrado', status=400)
        cursor.execute(
            "DELETE FROM db_clientes.tbl_clientes WHERE id =%s", (id))
        conn.commit()
        response = jsonify('Cliente deletado com sucesso!')
        response.status_code = 200
        return response
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

# API - Endereços

# Adicionando um registro de endereço - POST
@app.route('/enderecos', methods=['POST'])
@basic_auth.required
def add_endereco():
    try:
        _json = request.get_json(force=True)
        _idCliente = _json['idCliente']
        _rua = _json['rua']
        _numero = _json['numero']
        _bairro = _json['bairro']
        _cidade = _json['cidade']
        _estado = _json['estado']
        _cep = _json['cep']

        if _idCliente and _rua and _numero and _bairro and _cidade and _estado and _cep and request.method == 'POST':
            sqlQuery = "INSERT INTO db_clientes.tbl_enderecos(idCliente, rua, numero, bairro, cidade, estado, cep) VALUES(%s, %s, %s, %s, %s, %s, %s)"
            bindData = (_idCliente, _rua, _numero, _bairro,
                        _cidade, _estado, _cep)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Endereço cadastrado com sucesso!')
            respone.status_code = 200
            return respone
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.close()
        conn.close()

# Buscando todos os endereços cadastrados - GET
@app.route('/enderecos', methods=['GET'])
@basic_auth.required
def enderecos():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT idCliente, rua, numero, bairro, cidade, estado, cep, idEndereco FROM db_clientes.tbl_enderecos")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# Buscando um endereço cadastrado por meio de um ID - GET
@app.route('/enderecos/<int:idEndereco>', methods=['GET'])
@basic_auth.required
def endereco_cliente(idEndereco):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT idCliente, rua, numero, bairro, cidade, estado, cep, idEndereco FROM db_clientes.tbl_enderecos WHERE idEndereco=%s", idEndereco)
        empRows = cursor.fetchone()
        if not empRows:
            return Response('Endereço não encontrado', status=404)
        response = jsonify(empRows)
        response.status_code = 200
        return response
    except Exception as error:
        return error
    finally:
        cursor.close()
        conn.close()

# Alterando um endereço cadastrado - PUT
@app.route('/enderecos', methods=['PUT'])
@basic_auth.required
def update_endereco():
    try:
        _json = request.get_json(force=True)
        _idCliente = _json['idCliente']
        _idEndereco = _json['idEndereco']
        _rua = _json['rua']
        _numero = _json['numero']
        _bairro = _json['bairro']
        _cidade = _json['cidade']
        _estado = _json['estado']
        _cep = _json['cep']
        if _rua and _numero and _bairro and _cidade and _estado and _cep and _idCliente and _idEndereco and request.method == 'PUT':
            sqlQuery = "UPDATE db_clientes.tbl_enderecos SET rua=%s, numero=%s, bairro=%s, cidade=%s, estado=%s, cep=%s, idCliente=%s WHERE idEndereco=%s"
            bindData = (_rua, _numero, _bairro, _cidade,
                        _estado, _cep, _idCliente, _idEndereco)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Dados alterados com sucesso!')
            response.status_code = 200
            return response
        else:
            return not_found()
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

# Deletando algum endereço cadastrado - DELETE
@app.route('/enderecos/<int:idEndereco>', methods=['DELETE'])
@basic_auth.required
def delete_endereco(idEndereco):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlQuery = "SELECT * FROM db_clientes.tbl_enderecos WHERE idEndereco=%s"
        cursor.execute(sqlQuery, idEndereco)
        select = cursor.fetchone()
        if not select:
            return Response('Endereço não cadastrado', status=400)
        cursor.execute(
            "DELETE FROM db_clientes.tbl_enderecos WHERE idEndereco =%s", (idEndereco))
        conn.commit()
        respone = jsonify('Endereço deletado com sucesso!')
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# Busca de endereços por ID do cliente - GET
@app.route('/enderecos/clientes/<int:id>', methods=['GET'])
@basic_auth.required
def ligacao_cliente_enderecos(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT db_clientes.tbl_clientes.nome, db_clientes.tbl_enderecos.rua, db_clientes.tbl_enderecos.numero, db_clientes.tbl_enderecos.bairro, db_clientes.tbl_enderecos.cidade, db_clientes.tbl_enderecos.estado, db_clientes.tbl_enderecos.cep FROM db_clientes.tbl_clientes JOIN db_clientes.tbl_enderecos ON db_clientes.tbl_clientes.id = db_clientes.tbl_enderecos.idCliente WHERE id = %s", id)
        userRow = cursor.fetchall()
        if not userRow:
            return Response('Usuário/endereço não cadastrado', status=404)
        response = jsonify(userRow)
        response.status_code = 200
        return response
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        conn.close()


@app.errorhandler(404)
@basic_auth.required
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5100)
