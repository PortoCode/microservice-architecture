# Microservice Architecture

Application of a tourism agency with microservices architecture

# Technologies Deployed

1. Python
2. MySQL

# Run project

You **must to create** the .env file and set the environment variables. Below you can see an example of the .env file.

```bash
BASIC_AUTH_USERNAME=
BASIC_AUTH_PASSWORD=
MYSQL_DATABASE_HOST=localhost
MYSQL_DATABASE_USER=
MYSQL_DATABASE_PASSWORD=
MYSQL_DATABASE_DB_CLIENTES=db_clientes
MYSQL_DATABASE_DB_PRODUTOS=db_produtos
MYSQL_DATABASE_DB_VENDAS=db_vendas
clientes_rota=localhost:5100
cursos_rota=localhost:5300
```

To run the application go into the app folder.

```bash
cd app
```

Start each service on a different terminal.

```bash
py clientes.py
py enderecos.py
py produtos.py
py vendas.py
```

Access the data via Browser or Postman - remembering that the database needs to be installed and the data needs to have been created on the local machine.

- http://localhost:5100/clientes
- http://localhost:5200/enderecos
- http://localhost:5300/produtos
- http://localhost:5400/vendas
