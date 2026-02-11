class Product:
    def __init__(self, sku, name, price, qtd):
        self._sku = sku
        self._nome = name
        self._price = price
        self._qtd = qtd

    def get_sku(self):
        return self._sku

    def get_price(self):
        return self._price

    def is_available(self):
        result = True if self._qtd > 0 else False
        return result

