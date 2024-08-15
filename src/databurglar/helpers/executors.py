from sqlalchemy import ChunkedIteratorResult, Engine, Select
from sqlalchemy.orm import Session


def insert(engine: Engine, *args) -> None:
    with Session(engine) as session:
        session.add_all(args)
        session.commit()


def query(engine: Engine, statement: Select) -> ChunkedIteratorResult:
    with Session(engine) as session:
        return session.execute(statement)
