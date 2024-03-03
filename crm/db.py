import psycopg2
from psycopg2 import DatabaseError, sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT, connection


def get_admin_connection() -> connection:
    try:

        db_connect = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="123",
            host="localhost",
            port="5432",
        )
        db_connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return db_connect

    except DatabaseError as e:
        print(f"Error connecting to the database {e}")
        raise


def create_database(db_connect: connection):
    cursor_object = None
    try:
        cursor_object = db_connect.cursor()
        cursor_object.execute(
            sql.SQL("CREATE DATABASE {}").format(sql.Identifier("crm"))
        )
        print("Database crm created!")
    except DatabaseError as e:
        print(f"Error at creating database {e}")
    finally:
        if cursor_object:
            cursor_object.close()
        db_connect.close()


def drop_database(db_connect: connection, db_name: str):
    cursor_object = None

    try:
        cursor_object = db_connect.cursor()
        cursor_object.execute(
            sql.SQL("DROP DATABASE IF EXISTS {}").format(sql.Identifier(db_name))
        )
        print(f"Drop database {db_name} complete")
    except DatabaseError as e:
        print(f"Error at connecting to database {e}")
    finally:
        if cursor_object:
            cursor_object.close()

        db_connect.close()


admin_connect = get_admin_connection()

if admin_connect:
    create_database(admin_connect)
