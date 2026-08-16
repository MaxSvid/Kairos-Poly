import os
from psycopg import connect, OperationalError

from backend.settings import db_settings

def create_connection():
    try:
        connection = connect(
        )
        return connection
    except OperationalError as e:
        print(f"Connection error: {e}")