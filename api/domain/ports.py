from abc import ABC, abstractmethod
from typing import Any

class DeliveryFeeInboundPort(ABC):
    @abstractmethod
    def calculate_delivery_fee(self, cart_id: str) -> dict:
        pass

class CartPort(ABC):
    @abstractmethod
    def set_cart_items(self, items: Any):
        pass

    @abstractmethod
    def get_cart_items(self, cart_id: str):
        pass

class ProductMetadataPort(ABC):
    @abstractmethod
    def set_product_metadata(self, metadata: Any):
        pass

    @abstractmethod
    def get_product_metadata(self):
        pass

class CartValuePort(ABC):
    @abstractmethod
    def set_total_cart_value(self, value: float):
        pass

    @abstractmethod
    def get_total_cart_value(self, cart_id: str):
        pass
