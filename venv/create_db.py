import psycopg2
from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable

query1 = """CREATE DATABASE warsztat"""

query2 = """CREATE TABLE users(
    id serial PRIMARY KEY,
    username varchar(255),
    hashed_password varchar (80)
)"""

query3 = """CREATE TABLE messages(
    id serial PRIMARY KEY,
    creation_date timestamp DEFAULT current_timestamp,
    text varchar(255),
    from_id int,
    to_id int,
    FOREIGN KEY (from_id) REFERENCES users(id),
    FOREIGN KEY (to_id) REFERENCES users(id)
)"""

settings = {
    'host': 'localhost',
    'database': 'warsztat',
    'user': 'postgres',
    'password': 'coderslab',
    'port': 5432,
}

try:
    conn = connect(**settings)
    conn.autocommit = True
    cursor = conn.cursor()
    try:
        cursor.execute(query1)
        print("Database created successfully")
    except DuplicateDatabase as e:
        print("Database already exists", e)
except OperationalError as e:
    print("Connection error", e)

try:
    conn = connect(**settings)
    conn.autocommit = True
    cursor = conn.cursor()
    try:
        cursor.execute(query2)
        print("Table created successfully")
    except DuplicateTable as e:
        print("Table already exists", e)
except OperationalError as e:
    print("Connection error", e)

try:
    conn = connect(**settings)
    conn.autocommit = True
    cursor = conn.cursor()
    try:
        cursor.execute(query3)
        print("Table created successfully")
    except DuplicateTable as e:
        print("Table already exists", e)
except OperationalError as e:
    print("Connection error", e)
