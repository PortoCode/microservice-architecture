from app import app
from flaskext.mysql import MySQL
from flask_basicauth import BasicAuth
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app.config['BASIC_AUTH_USERNAME'] = os.environ['BASIC_AUTH_USERNAME']
app.config['BASIC_AUTH_PASSWORD'] = os.environ['BASIC_AUTH_PASSWORD']

auth = BasicAuth(app)

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = os.environ['MYSQL_DATABASE_USER']
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ['MYSQL_DATABASE_PASSWORD']
app.config['MYSQL_DATABASE_DB'] = os.environ['MYSQL_DATABASE_DB_CLIENTES']
app.config['MYSQL_DATABASE_DB'] = os.environ['MYSQL_DATABASE_DB_SERVICOS']
app.config['MYSQL_DATABASE_DB'] = os.environ['MYSQL_DATABASE_DB_PEDIDOS']
app.config['MYSQL_DATABASE_HOST'] = os.environ['MYSQL_DATABASE_HOST']


mysql.init_app(app)
