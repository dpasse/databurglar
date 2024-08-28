import os
import sys
import uuid
import pathlib
from datetime import datetime


sys.path.insert(0, os.path.join(pathlib.Path(__file__).parent.resolve(), '../src'))

from databurglar.models import setup_data_collection, setup_surveys, UserEvent
from databurglar.helpers.connection import connect_to_pg, DatabaseConnection
from databurglar.helpers.executors import insert, query
from databurglar.queries import tag

 
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

    ## add data

    data = [
        UserEvent(user_id=uuid.uuid4(), label='test', timestamp=datetime.now())
    ]

    insert(engine, *data)

    print(
        query(
            engine,
            tag.ByIds.generate({uuid.uuid4()})
        ).all()
    )
