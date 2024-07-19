# Project Setup Guide

## 1. Clone the Repository

Open your terminal and clone the repository:

```sh
git clone https://github.com/hurairaz/FastAPI-CRUD-PostgreSQL-Alembic.git
```

## 2. Open the Project in Your IDE

Open the cloned project in your preferred IDE (e.g., PyCharm).

## 3. Install Dependencies

Navigate to the project directory and install the required Python packages:

```sh
pip install -r requirements.txt
```

**Note:** The `psycopg2-binary` package is used to connect PostgreSQL with Python, and `alembic` is used for database migrations.

## 4. Install PostgreSQL

### On Ubuntu

Update your package list and install PostgreSQL:

```sh
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

Check the status of the PostgreSQL service:

```sh
service postgresql status
```

### Access PostgreSQL

Switch to the PostgreSQL user and access the PostgreSQL terminal:

```sh
sudo su postgres
psql
```

### Database Management

- **List Databases:**

  ```sh
  \l
  ```

- **List Users(Get your username):**

  ```sh
  \du
  ```

- **Set Password:**

  ```sql
  ALTER USER postgres WITH PASSWORD 'new_password';
  ```

- **Get Hostname:**

  ```sql
  SHOW listen_addresses;
  ```

- **Create a New Database:**

  ```sql
  CREATE DATABASE database_name;
  ```

- **Verify the Database:**

  ```sh
  \l
  ```

## 5. Initialize Alembic

Initialize Alembic for database migrations:

```sh
alembic init alembic
```

## 6. Configure Database URL

### In `database.py`

Add your PostgreSQL database URL:

```python
SQLALCHEMY_DATABASE_URL = "postgresql://username:password@hostname/database_name"
```

**Note:** In this project, the URL is stored in a `.env` file and accessed from there.

### In `alembic.ini`

Add the PostgreSQL database URL:

```ini
sqlalchemy.url = "postgresql://username:password@hostname/database_name"
```

## 7. Configure Alembic

### In `env.py` in the Alembic Folder

Update the `env.py` file to include your models:

```python
from database import Base
from models import *

target_metadata = Base.metadata
```

This configuration connects your tables in `models.py` to your PostgreSQL database.

## 8. Verify the Database Schema

### Access PostgreSQL

Switch to the PostgreSQL user and access the database:

```sh
sudo su postgres
psql
```

- **Connect to Your Database:**

  ```sh
  \c database_name
  ```

- **See Tables:**

  ```sh
  \dt
  ```

- **Open a Specific Table:**

  ```sh
  \d table_name
  ```
