from typing import cast

from sqlalchemy import Engine

from .base import AbstractService
from .. import queries
from ..models import Tag, AbstractEvent
from ..models.data import Data
from ..validators.services import TagValidatorService


class CreationService(AbstractService):
    def __init__(self, engine: Engine, tag_validator: TagValidatorService) -> None:
        super().__init__(engine)

        self._tag_validator = tag_validator

    def create(self, request: Data[AbstractEvent]) -> None:
        tags = self.session.query(Tag) \
            .filter(
                Tag.id.in_(
                    set(item.tag_id for item in request.items)
                )
            ) \
            .all()

        tag_lookup = {tag.id: tag for tag in tags}

        self.session.add(request.event)

        for item in request.items:
            tag = tag_lookup.get(item.tag_id)
            if tag is None:
                raise Exception(f'Tag "{item.tag_id}" could not be found.')

            item.event_id = request.event.id
            item.is_valid = self._tag_validator.validate(tag, item.get_value(tag))

        self.session.add_all(request.items)
        self.session.commit()
