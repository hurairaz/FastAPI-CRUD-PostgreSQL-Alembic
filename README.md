# Project Setup Guide

This guide covers the steps to set up a FastAPI project with PostgreSQL and Alembic for database migrations.

## 1. Install PostgreSQL

### Update Package List
```sh
sudo apt-get update
```

### Install PostgreSQL and Contrib Package
```sh
sudo apt-get install postgresql postgresql-contrib
```

### Check PostgreSQL Service Status
```sh
service postgresql status
```

### Open PostgreSQL in Terminal
```sh
sudo su postgres
psql
```

### List of Databases
```sql
\l
```

### List of Users
```sql
\du
```

### Set Password for User (e.g., `postgres`)
```sql
ALTER USER postgres WITH PASSWORD 'new_password';
```

### Get Hostname
```sql
SHOW listen_addresses;
```

### Create Database
```sql
CREATE DATABASE database_name;
```

### Verify Your Database in the List
```sql
\l
```

## 2. Install PostgreSQL Adapter to Connect with Python Code
```sh
pip install psycopg2-binary
```

## 3. Install Alembic
```sh
pip install alembic
alembic init alembic
```

## 4. Configure Database URL in `database.py`
```python
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@hostname/database_name"
```

## 5. Configure Database URL in `alembic.ini`
Open `alembic.ini` and update:
```ini
sqlalchemy.url = postgresql://username:password@hostname/database_name
```

## 6. Update `env.py` in Alembic Folder
Add the following imports and configuration:
```python
from database import Base
from models import *
target_metadata = Base.metadata
```

## 7. Verify Connection and Tables

### Open PostgreSQL in Terminal
```sh
sudo su postgres
psql
```

### Verify Your Database Exists in the List
```sql
\l
```

### Connect to Database
```sql
\c database_name
```

### See Tables (Tables in models.py should reflect here)
```sql
\dt
```

### Open a Specific Table
```sql
\d table_name
```

---
