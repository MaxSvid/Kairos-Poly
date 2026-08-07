import os
from psycopg import connect, OperationalError

from backend.settings import db_settings

def create_connection():
    try:
        connection = connect(
            user=db_settings.POSTGRES_USER,
            password=db_settings.POSTGRES_PASSWORD,
            host=db_settings.POSTGRES_HOST,
            dbname=db_settings.POSTGRES_PORT
        )
        return connection
    except OperationalError as e:
        print(f"Connection error: {e}")