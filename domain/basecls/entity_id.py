import abc
from datetime import datetime
from typing import TypeVar, Type, cast
from .valueobject import ValueObject


class EntityId(ValueObject):

    @abc.abstractmethod
    def __init__(self, identifier: str) -> None:
        self._identifier = identifier

    @property
    def identifier(self) -> str:
        return self._identifier

    def __eq__(self, other: object) -> bool:
        if other is None: return False
        if type(self) != type(other): return False
        other = cast(EntityId, other)
        return (self.identifier) == (other.identifier)

    def __hash__(self) -> int:
        return hash((self.identifier))
