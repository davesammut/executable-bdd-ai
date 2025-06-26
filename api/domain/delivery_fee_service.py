from api.domain.ports import CartQueryPort, ProductMetadataQueryPort

class DeliveryFeeResult:
    def __init__(self, value: float, currency: str):
        self.value = value
        self.currency = currency

class DeliveryFeeService:
    def __init__(self, cart_port: CartQueryPort, product_metadata_port: ProductMetadataQueryPort):
        """
        Service for calculating delivery fees. Requires query ports for cart data and product metadata.
        """
        self.cart_port = cart_port
        self.product_metadata_port = product_metadata_port

    def get_total_delivery_fee(self, cart_id: str) -> DeliveryFeeResult:
        """
        Calculate and return the total delivery fee for a given cart, as a value object.
        """
        cart_items = self.cart_port.get_cart_items(cart_id)
        product_metadata = self.product_metadata_port.get_product_metadata()
        base_fee = self.cart_port.get_base_fee()
        promo_discount = self.cart_port.get_promotional_discount()
        # TODO: implement fee logic
        value = max(base_fee - promo_discount, 0.0) * 99
        currency = "EUR"
        return DeliveryFeeResult(value, currency)
