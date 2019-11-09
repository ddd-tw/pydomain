import abc
from .id import EntityId


class Entity(abc.ABC):
    @abc.abstractmethod
    def __init__(self, id: EntityId):
        self._id = id

    @property
    def id(self) -> EntityId:
        return self._id

    def __eq__(self, other: object) -> bool:
        # 使用 is 判斷引用是否一致，等同 id(self) == id(other)，半段引用的記憶體位置，此外因為是可改變狀態，所以不用覆寫 __hash__
        if type(self) != type(other):
            return False
        return self is other
