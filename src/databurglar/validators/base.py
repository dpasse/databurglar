from abc import ABC, abstractmethod

from ..models import DataReturnType, Tag


class AbstractTagValidator(ABC):
    @property
    @abstractmethod
    def key(self) -> str:
        pass

    @abstractmethod
    def validate(self, tag: Tag, value: DataReturnType | None) -> bool:
        pass
