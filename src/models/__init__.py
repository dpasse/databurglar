from .base import Base
from .enums import DataType
from .event import UserEvent
from .data_point import DataPoint
from .data import DataStore
from .survey import Survey
from .survey_question import SurveyQuestion

from sqlalchemy import Engine


def setup_data_collection(engine: Engine, event_table: Base):
    Base.metadata.create_all(engine, tables=[
        event_table.__table__,
        DataPoint.__table__,
        DataStore.__table__
    ])

def setup_surveys(engine: Engine):
    Base.metadata.create_all(engine, tables=[
        Survey.__table__,
        SurveyQuestion.__table__
    ])
