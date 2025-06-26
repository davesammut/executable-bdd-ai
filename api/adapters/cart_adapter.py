from api.domain.ports import CartPort, CartValuePort
from typing import Any

class CartAdapter:
    """
    Adapter for cart operations, delegating calls to the underlying ports.
    """
    def __init__(self, cart_port: CartPort, cart_value_port: CartValuePort):
        self.cart_port = cart_port
        self.cart_value_port = cart_value_port

    def set_cart_items(self, items: Any):
        self.cart_port.set_cart_items(items)

    def get_cart_items(self, cart_id: str):
        return self.cart_port.get_cart_items(cart_id)


    def set_total_cart_value(self, value: float):
        self.cart_value_port.set_total_cart_value(value)

    def get_total_cart_value(self, cart_id: str):
        return self.cart_value_port.get_total_cart_value(cart_id)

    def get_base_fee(self) -> float:
        """Returns the base delivery fee."""
        return 99.00

    def get_promotional_discount(self) -> float:
        """Returns the promotional discount amount."""
        return 88.00
