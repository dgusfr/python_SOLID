from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List
from src.domain.entities.cart import Cart

T = TypeVar('T')

class GetRepositoryProtocol(ABC, Generic[T]):
    @abstractmethod
    def read(self, item_id: str) -> T:
        pass


class GetAllRepositoryProtocols(ABC,  Generic[T]):
    @abstractmethod
    def read_all(self) -> List[T]:
        pass


class InsertRepositoryProtocol(ABC,  Generic[T]):
    @abstractmethod
    def save(self, data: T):
        pass


class DeleteRepositoryProtocol(ABC, Generic[T]):
    @abstractmethod
    def delete(self, item_id: str):
        pass


class UpdateRepositoryProtocol(ABC, Generic[T]):
    @abstractmethod
    def update(self, data: T, item_id: str):
        pass


class CartRepositoryProtocol(
    GetRepositoryProtocol[Cart],
    DeleteRepositoryProtocol[Cart],
    InsertRepositoryProtocol[Cart],
    UpdateRepositoryProtocol[Cart],
    ABC
):
    pass
