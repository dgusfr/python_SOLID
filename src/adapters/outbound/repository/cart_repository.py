from typing import List

from src.domain.ports.outbound.repository_protocol import (
    CartRepositoryProtocol
)
from src.domain.use_case.switch_cart_use_case import SwitchCartUseCase
from src.domain.entities.cart import Cart

LIST_CART: List[Cart] = []

class CartRepository(
        CartRepositoryProtocol
):
    def __init__(self):
        self._carts = LIST_CART

    def save(self, data: Cart):
        self._carts.append(data)

    def delete(self, item_id: str):
        result = [
            unique for unique in self._carts
            if unique.get_cart_id() == item_id
        ]
        self._carts.remove(result[0])

    def read(self, item_id: str):
        result = [
            unique for unique in self._carts
            if unique.get_cart_id() == item_id
        ]
        return result

    def update(self, item_id: str, data: Cart):
        result = [
            unique for unique in self._carts
            if unique.get_cart_id() == item_id
        ]
        self._carts.remove(result[0])
        self.save(data)
