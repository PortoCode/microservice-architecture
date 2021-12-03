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
MYSQL_DATABASE_DB_SERVICOS=db_servicos
MYSQL_DATABASE_DB_PEDIDOS=db_pedidos
clientes_rota=localhost:5100
servicos_rota=localhost:5200
```

To run the application go into the app folder.

```bash
cd app
```

Start each service on a different terminal.

```bash
py clientes.py
py servicos.py
py pedidos.py
```

Access the data via Browser or Postman - remembering that the database needs to be installed and the data needs to have been created on the local machine.

- http://localhost:5100/clientes
- http://localhost:5200/servicos
- http://localhost:5300/pedidos
