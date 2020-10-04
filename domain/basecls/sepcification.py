from typing import Callable, Any, List
from sutoppu import Specification


class PredicateSpecification(Specification):
    """
    傳入一個有任何參數且回傳布林值的 Function 作為判斷表示式
    """

    def __init__(self, predicate: Callable[..., Any]) -> None:
        super().__init__()
        self._predicate = predicate

    @property
    def predicate(self) -> Callable[..., Any]:
        return self._predicate

    def is_satisfied_by(self, *candidate: List[Any]):
        return self._predicate(*candidate)
