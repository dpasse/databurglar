from typing import Optional

from sqlalchemy import Engine
from sqlalchemy.orm import Session


class AbstractService:
    def __init__(self, engine: Engine) -> None:
        self._engine = engine
        self._session: Optional[Session] = None

    @property
    def session(self) -> Session:
        if self._session is None:
            raise Exception('A session must first be started.')

        return self._session

    def __enter__(self) -> 'AbstractService':
        self._session = Session(self._engine)
        return self

    def __exit__(self, type, value, traceback):
        self.session.close()
