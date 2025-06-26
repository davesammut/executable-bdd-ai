from abc import ABC, abstractmethod
from typing import Any

class DeliveryFeeInboundPort(ABC):
    @abstractmethod
    def calculate_delivery_fee(self, cart_id: str) -> dict:
        pass

class CartQueryPort(ABC):
    @abstractmethod
    def get_cart_items(self, cart_id: str):
        pass

    @abstractmethod
    def get_total_cart_value(self, cart_id: str):
        pass

    @abstractmethod
    def get_base_fee(self) -> float:
        pass

    @abstractmethod
    def get_promotional_discount(self) -> float:
        pass

class CartCommandPort(ABC):
    @abstractmethod
    def set_cart_items(self, cart_id: str, items: Any):
        pass

    @abstractmethod
    def set_total_cart_value(self, cart_id: str, value: float):
        pass

class ProductMetadataQueryPort(ABC):
    @abstractmethod
    def get_product_metadata(self):
        pass

class ProductMetadataCommandPort(ABC):
    @abstractmethod
    def set_product_metadata(self, metadata: Any):
        pass

class CartValuePort(ABC):
    pass
