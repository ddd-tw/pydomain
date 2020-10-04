import abc


class ValueObject(abc.ABC):

    @abc.abstractmethod
    def __eq__(self, other: object):
        raise NotImplementedError("Please implement __equal__")

    @abc.abstractmethod
    def __hash__(self):
        raise NotImplementedError("Please implement __hash__")
