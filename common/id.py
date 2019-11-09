import abc
from typing import TypeVar, Type, cast
from datetime import datetime
from .valueobj import ValueObject
from plugin.date import formatter


class EntityId(ValueObject):
    @abc.abstractmethod
    def __init__(self, code: str, serial_no: int, createtd_at: datetime) -> None:
        self._code = code
        # TODO: 客製化 Error Code 與 Message
        if serial_no < 0:
            raise ValueError("Serial No must larger than 0.")
        self._serial_no = serial_no
        self._createtd_at = createtd_at

    @property
    def code(self) -> str:
        return self._code

    @property
    def serial_no(self) -> int:
        return self._serial_no

    @property
    def createtd_at(self) -> datetime:
        return self._createtd_at

    def __eq__(self, other: object) -> bool:
        if type(self) is type(other):
            return False
        other = cast(EntityId, other)
        return (self.code, self.createtd_at, self.serial_no) == \
            (other.code, other.createtd_at, other.serial_no)

    def __hash__(self) -> int:
        return hash((self.code, self.createtd_at, self.serial_no))

    def __str__(self) -> str:
        # 取得字串型別的 Entity Id
        createtd_at = self.createtd_at.strftime("%Y%m%d")
        return "{code}-{date}-{sn}" \
            .format(code=self.code, date=self.createtd_at, sn=self.serial_no)

    def __repr__(self) -> str:
        return "<{class}: code={code}, createtd_at={date}, serial_no={sn}" \
            .format(type(self).__name__, code=self.code, date=self.createtd_at, sn=self.serial_no)

    # TODO: 實現 Iterable
