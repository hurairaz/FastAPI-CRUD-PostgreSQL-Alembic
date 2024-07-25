# Integrating FastAPI with SQLAlchemy-PostgreSQL and Alembic

This repository provides a detailed guide on integrating a FastAPI application with a PostgreSQL database using SQLAlchemy for ORM and Alembic for database migrations

## Project Structure

The project structure is as follows:

```
Integrating-FastAPI-with-SQLAlchemy-PostgreSQL-and-Alembic
├── fastapi_postgres-app
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
│   └── alembic.ini
├── alembic
│   ├── versions
│   │   └── env.py
│   │   └── script.py.mako
│   └── README
└── README.md
```

## Getting Started

To get started with the project, first clone the repository to your local machine:

```sh
git clone https://github.com/hurairaz/Integrating-FastAPI-with-SQLAlchemy-PostgreSQL-and-Alembic.git
```

Once cloned, navigate to the project directory and install the required Python packages using:

```sh
pip install -r requirements.txt
```

**Note:** The `psycopg2-binary` package is used for connecting PostgreSQL with Python, and `alembic` is used for handling database migrations.

## Setting Up PostgreSQL

On Ubuntu, you can update your package list and install PostgreSQL with:

```sh
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

After installation, check the status of the PostgreSQL service:

```sh
service postgresql status
```

To configure PostgreSQL, switch to the PostgreSQL user and access the PostgreSQL terminal:

```sh
sudo su postgres
psql
```

In the PostgreSQL terminal, you can list users to get your username with:

```sh
postgres=# \du
```

Set the password for the `postgres` user:

```sql
postgres=# ALTER USER postgres WITH PASSWORD 'new_password';
```

To get the hostname, use:

```sql
postgres=# SHOW listen_addresses;
```

Create a new database:

```sql
postgres=# CREATE DATABASE database_name;
```

Verify the database creation with:

```sh
postgres=# \l
```

With your PostgreSQL username, password, hostname, and database name, you can now connect your FastAPI application to the database and initialize Alembic for database migrations.

## Configuring FastAPI and Alembic

Initialize Alembic for database migrations with:

```sh
alembic init alembic
```

In the `database.py` file, add your PostgreSQL database URL:

```python
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@hostname/database_name"
```

**Note:** In this project, the URL is stored in a `.env` file and accessed from there.

In the `alembic.ini` file, update the PostgreSQL database URL:

```ini
sqlalchemy.url = postgresql://username:password@hostname/database_name
```

Then, in the `env.py` file located in the Alembic folder, update it to include your models:

```python
from database import Base
target_metadata = Base.metadata
```

This configuration ensures that Alembic connects your tables defined in `models.py` to your PostgreSQL database. 

To apply the initial database migration, run:

```sh
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

To verify the setup, check if the database contains the tables you defined in `models.py`. Open your terminal and connect to the database:

```sh
sudo su postgres
psql
```

Connect to your database with:

```sh
postgres=# \c database_name
```

List the tables with:

```sh
postgres=# \dt
```

To view the details of a specific table, use:

```sh
postgres=# \d table_name
```

This will ensure that your tables from `models.py` are properly reflected in the database.

## Running the Application

To run the FastAPI application, open a terminal in your project directory and execute:

```sh
uvicorn main:app --reload
```

This will start the FastAPI server, and you can access your application at `http://127.0.0.1:8000`.

---
