import psycopg2
from psycopg2.extensions import connection


def get_database_connection() -> connection:
    return psycopg2.connect(
        dbname="crm", user="root", password="password", host="localhost", port="5432"
    )


cursorObj = get_database_connection().cursor()

cursorObj.execute("CREATE DATABASE crm")

print("Database crm created successfully")
