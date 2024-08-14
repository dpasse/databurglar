import os
import sys


sys.path.insert(0, os.path.join('../src'))

from models import setup_data_collection, setup_surveys, UserEvent
from helpers.connection import connect_to_pg, DatabaseConnection

 
if __name__ == '__main__':
    engine = connect_to_pg(
        DatabaseConnection(
            user = 'postgres',
            password = 'password',
            host = 'localhost',
            port = 5432,
            database = 'qa-test'
        )
    )

    setup_data_collection(engine, UserEvent)
    setup_surveys(engine)
