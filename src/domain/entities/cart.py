from enum import StrEnum, auto
from typing import List, Optional
from uuid import uuid4

from src.domain.entities.product import Product


class CartStatus(StrEnum):
    ACTIVE = auto()
    FINISHED = auto()
    EXPIRED = auto()


class Cart:
    def __init__(self, products: List[Product], cart_id: Optional[uuid4] = None):
        self._products = products
        self._cart_id = cart_id
        self._status = CartStatus.ACTIVE

    def get_cart_id(self):
        if self._cart_id is None:
            self._cart_id = uuid4()
        return self._cart_id

    def add_new_product(self, produto: Product):
        self._products.append(produto)

    def remove_product(self, produto: Product):
        self._products.remove(produto)

    def _cal_subtotal(self):
        prices = [
            produto.get_price() for produto in self._products if produto.is_available()
        ]
        total = sum(prices)
        self._subtotal = total
        return total

    def get_subtotal(self):
        self._cal_subtotal()
        return self._subtotal

    def get_status(self):
        return self._status

    def switch(self, novo_status):
        self._status = novo_status
        return self._status


