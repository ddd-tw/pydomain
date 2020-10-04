import json
from .code import DomainErrorCode
from typing import Optional


class DomainException(Exception):
    def __init__(self,
                 error_code: DomainErrorCode,
                 inner: Optional[Exception] = None,
                 stack_trace: Optional[str] = None,
                 data: Optional[dict] = None) -> None:
        self._error_code = error_code.name
        self._error_message = error_code.value
        self._inner = inner
        self._stack_trace = stack_trace
        self._data = data

    @property
    def error_code(self) -> str:
        return self._error_code

    @property
    def error_message(self) -> str:
        return self._error_message

    @property
    def inner(self) -> Optional[Exception]:
        return self._inner

    @property
    def stack_trace(self) -> Optional[str]:
        return self._stack_trace

    @property
    def data(self) -> Optional[dict]:
        return self._data

    def __str__(self) -> str:
        return "<inner: {inner}, code: {code}, message: {message}, data: {data}>".format(inner=self.inner,
                                                                                         code=self.error_code,
                                                                                         message=self.error_message,
                                                                                         data=json.dumps(self.data))

    def __repr__(self) -> str:
        return "<DomainException:\n\
                code: {code} \n\
                message: {message} \n\
                inner={inner}\n\
                stack_trace={trace}\n\
                data={data}>".format(code=self.error_code,
                                     message=self.error_message,
                                     inner=type(self.inner).__name__ if self.inner else None,
                                     trace=type(self.stack_trace).__name__ if self.inner else None,
                                     data=self.data if self.data else None)

