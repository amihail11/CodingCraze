from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar("T")


class IStack(Generic[T], ABC):
    @abstractmethod
    def push(self, value: T) -> None:
        pass

    @abstractmethod
    def pop(self) -> T:
        pass

    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def empty(self) -> bool:
        pass

    @abstractmethod
    def print(self) -> None:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass
