import os
import sys

from sqlalchemy import create_engine, Engine


sys.path.insert(0, os.path.join('../src'))

from models import setup_db


user = 'postgres'
password = 'password'
host = 'localhost'
port = 5432
database = 'qa-test'


def get_connection() -> Engine:
    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )
 
 
if __name__ == '__main__':
    engine = get_connection()

    setup_db(engine)
