import pymysql
from app import app
from config import mysql, auth
from flask import jsonify, Response, Flask, request
from flask_debug import Debug
from flask_basicauth import BasicAuth

basic_auth = auth

# ----------> BILHETES TURÍSTICOS <----------

# Adicionando um registro de bilhete - POST
@app.route('/servicos/bilhetes', methods=['POST'])
@basic_auth.required
def add_bilhete():
    try:
        _json = request.get_json(force=True)
        _descricao = _json['descricao']
        _data = _json['data']
        _preco = _json['preco']

        if _descricao and _data and _preco and request.method == 'POST':
            sqlQuery = "INSERT INTO db_servicos.tbl_bilhetes (descricao, data, preco) VALUES (%s,%s,%s)"
            bindData = (_descricao, _data, _preco)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Bilhete adicionado com sucesso!')
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

# Retornando todos os registros de bilhetes - GET
@app.route('/servicos/bilhetes', methods=['GET'])
# @basic_auth.required
def get_bilhetes():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT idBilhete, descricao, data, preco FROM db_servicos.tbl_bilhetes")
        userRows = cursor.fetchall()
        response = jsonify(userRows)
        response.status_code == 200
        return response
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

# Retornando o registro de bilhete de um ID específico - GET
@app.route('/servicos/bilhetes/<int:id>',  methods=['GET'])
@basic_auth.required
def id_bilhete(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT idBilhete, descricao, data, preco FROM db_servicos.tbl_bilhetes WHERE idBilhete =%s", id)
        userRow = cursor.fetchone()
        if not userRow:
            return Response('Bilhete não cadastrado', status=404)
        response = jsonify(userRow)
        response.status_code == 200
        return response
    except Exception as error:
        return error
    finally:
        cursor.close()
        conn.close()

# Alterando algum bilhete cadastrado - PUT
@app.route('/servicos/bilhetes', methods=['PUT'])
@basic_auth.required
def update_bilhete():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _json = request.get_json(force=True)
        _idBilhete = _json['idBilhete']
        _descricao = _json['descricao']
        _data = _json['data']
        _preco = _json['preco']

        if _descricao and _data and _preco and _idBilhete and request.method == 'PUT':
            sqlQuery = "SELECT * FROM db_servicos.tbl_bilhetes WHERE idBilhete=%s"
            cursor.execute(sqlQuery, _idBilhete)
            select = cursor.fetchone()
            if not select:
                return Response('Bilhete não cadastrado', status=400)
            sqlQuery = "UPDATE db_servicos.tbl_bilhetes SET descricao=%s, data=%s, preco=%s WHERE idBilhete=%s"
            bindData = (_descricao, _data, _preco, _idBilhete)
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

# Deletando algum bilhete - DELETE
@app.route('/servicos/bilhetes/<int:id>', methods=['DELETE'])
@basic_auth.required
def delete_bilhete(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlQuery = "SELECT * FROM db_servicos.tbl_bilhetes WHERE idBilhete=%s"
        cursor.execute(sqlQuery, id)
        select = cursor.fetchone()
        if not select:
            return Response('Bilhete não cadastrado', status=400)
        cursor.execute(
            "DELETE FROM db_servicos.tbl_bilhetes WHERE idBilhete =%s", (id))
        conn.commit()
        respone = jsonify('Bilhete deletado com sucesso!')
        respone.status_code = 200
        return respone
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        conn.close()


# ----------> HOSPEDAGENS <----------

# Adicionando um registro de hospedagem - POST
@app.route('/servicos/hospedagens', methods=['POST'])
@basic_auth.required
def add_hospedagem():
    try:
        _json = request.get_json(force=True)
        _endereco = _json['endereco']
        _data = _json['data']
        _preco = _json['preco']

        if _endereco and _data and _preco and request.method == 'POST':
            sqlQuery = "INSERT INTO db_servicos.tbl_hospedagens (endereco, data, preco) VALUES (%s,%s,%s)"
            bindData = (_endereco, _data, _preco)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Hospedagem adicionada com sucesso!')
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

# Retornando todos os registros de hospedagens - GET
@app.route('/servicos/hospedagens', methods=['GET'])
# @basic_auth.required
def get_hospedagens():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT idHospedagem, endereco, data, preco FROM db_servicos.tbl_hospedagens")
        userRows = cursor.fetchall()
        response = jsonify(userRows)
        response.status_code == 200
        return response
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

# Retornando o registro de hospedagem de um ID específico - GET
@app.route('/servicos/hospedagens/<int:id>',  methods=['GET'])
@basic_auth.required
def id_hospedagem(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT idHospedagem, endereco, data, preco FROM db_servicos.tbl_hospedagens WHERE idHospedagem =%s", id)
        userRow = cursor.fetchone()
        if not userRow:
            return Response('Hospedagem não cadastrada', status=404)
        response = jsonify(userRow)
        response.status_code == 200
        return response
    except Exception as error:
        return error
    finally:
        cursor.close()
        conn.close()

# Alterando alguma hospedagem cadastrada - PUT
@app.route('/servicos/hospedagens', methods=['PUT'])
@basic_auth.required
def update_hospedagem():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _json = request.get_json(force=True)
        _idHospedagem = _json['idHospedagem']
        _endereco = _json['endereco']
        _data = _json['data']
        _preco = _json['preco']

        if _endereco and _data and _preco and _idHospedagem and request.method == 'PUT':
            sqlQuery = "SELECT * FROM db_servicos.tbl_hospedagens WHERE idHospedagem=%s"
            cursor.execute(sqlQuery, _idHospedagem)
            select = cursor.fetchone()
            if not select:
                return Response('Bilhete não cadastrado', status=400)
            sqlQuery = "UPDATE db_servicos.tbl_hospedagens SET endereco=%s, data=%s, preco=%s WHERE idHospedagem=%s"
            bindData = (_endereco, _data, _preco, _idHospedagem)
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

# Deletando alguma hospedagem - DELETE
@app.route('/servicos/hospedagens/<int:id>', methods=['DELETE'])
@basic_auth.required
def delete_hospedagem(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlQuery = "SELECT * FROM db_servicos.tbl_hospedagens WHERE idHospedagem=%s"
        cursor.execute(sqlQuery, id)
        select = cursor.fetchone()
        if not select:
            return Response('Hospedagem não cadastrada', status=400)
        cursor.execute(
            "DELETE FROM db_servicos.tbl_hospedagens WHERE idHospedagem =%s", (id))
        conn.commit()
        respone = jsonify('Hospedagem deletada com sucesso!')
        respone.status_code = 200
        return respone
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        conn.close()


# ----------> VEICULOS <----------

# Adicionando um registro de veiculo - POST
@app.route('/servicos/veiculos', methods=['POST'])
@basic_auth.required
def add_veiculo():
    try:
        _json = request.get_json(force=True)
        _descricao = _json['descricao']
        _data = _json['data']
        _preco = _json['preco']

        if _descricao and _data and _preco and request.method == 'POST':
            sqlQuery = "INSERT INTO db_servicos.tbl_veiculos (descricao, data, preco) VALUES (%s,%s,%s)"
            bindData = (_descricao, _data, _preco)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Veículo adicionado com sucesso!')
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

# Retornando todos os registros de veiculos - GET
@app.route('/servicos/veiculos', methods=['GET'])
# @basic_auth.required
def get_veiculos():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT idVeiculo, descricao, data, preco FROM db_servicos.tbl_veiculos")
        userRows = cursor.fetchall()
        response = jsonify(userRows)
        response.status_code == 200
        return response
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

# Retornando o registro de veiculo de um ID específico - GET
@app.route('/servicos/veiculos/<int:id>',  methods=['GET'])
@basic_auth.required
def id_veiculo(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT idVeiculo, descricao, data, preco FROM db_servicos.tbl_veiculos WHERE idVeiculo =%s", id)
        userRow = cursor.fetchone()
        if not userRow:
            return Response('Veículo não cadastrado', status=404)
        response = jsonify(userRow)
        response.status_code == 200
        return response
    except Exception as error:
        return error
    finally:
        cursor.close()
        conn.close()

# Alterando algum veiculo cadastrado - PUT
@app.route('/servicos/veiculos', methods=['PUT'])
@basic_auth.required
def update_veiculo():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _json = request.get_json(force=True)
        _idVeiculo = _json['idVeiculo']
        _descricao = _json['descricao']
        _data = _json['data']
        _preco = _json['preco']

        if _descricao and _data and _preco and _idVeiculo and request.method == 'PUT':
            sqlQuery = "SELECT * FROM db_servicos.tbl_veiculos WHERE idVeiculo=%s"
            cursor.execute(sqlQuery, _idVeiculo)
            select = cursor.fetchone()
            if not select:
                return Response('Veículo não cadastrado', status=400)
            sqlQuery = "UPDATE db_servicos.tbl_veiculos SET descricao=%s, data=%s, preco=%s WHERE idVeiculo=%s"
            bindData = (_descricao, _data, _preco, _idVeiculo)
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

# Deletando algum veiculo - DELETE
@app.route('/servicos/veiculos/<int:id>', methods=['DELETE'])
@basic_auth.required
def delete_veiculo(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlQuery = "SELECT * FROM db_servicos.tbl_veiculos WHERE idVeiculo=%s"
        cursor.execute(sqlQuery, id)
        select = cursor.fetchone()
        if not select:
            return Response('Veículo não cadastrado', status=400)
        cursor.execute(
            "DELETE FROM db_servicos.tbl_veiculos WHERE idVeiculo =%s", (id))
        conn.commit()
        respone = jsonify('Veículo deletado com sucesso!')
        respone.status_code = 200
        return respone
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        conn.close()


# ----------> PASSAGENS <----------

# Adicionando um registro de passagem - POST
@app.route('/servicos/passagens', methods=['POST'])
@basic_auth.required
def add_passagem():
    try:
        _json = request.get_json(force=True)
        _origem = _json['origem']
        _destino = _json['destino']
        _data = _json['data']
        _preco = _json['preco']

        if _origem and _destino and _data and _preco and request.method == 'POST':
            sqlQuery = "INSERT INTO db_servicos.tbl_passagens (origem, destino, data, preco) VALUES (%s,%s,%s,%s)"
            bindData = (_origem, _destino, _data, _preco)
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Passagem adicionada com sucesso!')
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

# Retornando todos os registros de passagens - GET
@app.route('/servicos/passagens', methods=['GET'])
# @basic_auth.required
def get_passagens():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT idPassagem, origem, destino, data, preco FROM db_servicos.tbl_passagens")
        userRows = cursor.fetchall()
        response = jsonify(userRows)
        response.status_code == 200
        return response
    except Exception as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

# Retornando o registro de passagem de um ID específico - GET
@app.route('/servicos/passagens/<int:id>',  methods=['GET'])
@basic_auth.required
def id_passagem(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT idPassagem, origem, destino, data, preco FROM db_servicos.tbl_passagens WHERE idPassagem =%s", id)
        userRow = cursor.fetchone()
        if not userRow:
            return Response('Passagem não cadastrada', status=404)
        response = jsonify(userRow)
        response.status_code == 200
        return response
    except Exception as error:
        return error
    finally:
        cursor.close()
        conn.close()

# Alterando alguma passagem cadastrada - PUT
@app.route('/servicos/passagens', methods=['PUT'])
@basic_auth.required
def update_passagem():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        _json = request.get_json(force=True)
        _idPassagem = _json['idPassagem']
        _origem = _json['origem']
        _destino = _json['destino']
        _data = _json['data']
        _preco = _json['preco']

        if _origem and _destino and _data and _preco and _idPassagem and request.method == 'PUT':
            sqlQuery = "SELECT * FROM db_servicos.tbl_passagens WHERE idPassagem=%s"
            cursor.execute(sqlQuery, _idPassagem)
            select = cursor.fetchone()
            if not select:
                return Response('Passagem não cadastrada', status=400)
            sqlQuery = "UPDATE db_servicos.tbl_passagens SET origem=%s, destino=%s, data=%s, preco=%s WHERE idPassagem=%s"
            bindData = (_origem, _destino, _data, _preco, _idPassagem)
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

# Deletando alguma passagem - DELETE
@app.route('/servicos/passagens/<int:id>', methods=['DELETE'])
@basic_auth.required
def delete_passagem(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        sqlQuery = "SELECT * FROM db_servicos.tbl_passagens WHERE idPassagem=%s"
        cursor.execute(sqlQuery, id)
        select = cursor.fetchone()
        if not select:
            return Response('Passagem não cadastrada', status=400)
        cursor.execute(
            "DELETE FROM db_servicos.tbl_passagens WHERE idPassagem =%s", (id))
        conn.commit()
        respone = jsonify('Passagem deletada com sucesso!')
        respone.status_code = 200
        return respone
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
    app.run(debug=True, host="0.0.0.0", port=5200)
