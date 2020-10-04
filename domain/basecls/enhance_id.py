import abc
from typing import TypeVar, Type, cast
from datetime import datetime
from .entity_id import EntityId


class EntityEnhanceId(EntityId):
    DATE_FORMAT = "%Y%m%d"

    @abc.abstractmethod
    def __init__(self, code: str, serial_no: int, createtd_at: datetime) -> None:
        self._code = code
        if serial_no < 0:
            raise ValueError("Serial No. must larger than 0.")
        self._serial_no = serial_no
        self._createtd_at = createtd_at
        super(EntityEnhanceId, self).__init__(self._make_identifier())

    @classmethod
    def translate(cls, source: str) -> "EntityEnhanceId":
        slices = source.split("-")

        if len(slices) != 3:
            raise ValueError("Id format not correct.")

        code, serial_no, created_time = slices[0], slices[1], slices[2]

        if not serial_no.isdigit():
            raise ValueError("Id format not correct.")

        created_at: datetime

        try:
            created_at = datetime.strptime(created_time, cls.DATE_FORMAT)
        except Exception:
            raise ValueError("Id format not correct.")

        return cls(code, int(serial_no), created_at)

    def _make_identifier(self):
        # 取得字串型別的 Entity Id
        createtd_at = self.createtd_at.strftime(self.DATE_FORMAT)
        return "{code}-{date}-{sn}" \
            .format(code=self.code, date=self.createtd_at, sn=self.serial_no)

    @property
    def code(self) -> str:
        return self._code

    @property
    def serial_no(self) -> int:
        return self._serial_no

    @property
    def createtd_at(self) -> datetime:
        return self._createtd_at

    def __str__(self) -> str:
        return self._make_identifier()

    def __repr__(self) -> str:
        return "<{cls}: code={code}, createtd_at={date}, serial_no={sn}" \
            .format(cls=type(self).__name__, code=self.code, date=self.createtd_at, sn=self.serial_no)

    # TODO: 實現 Iterable
