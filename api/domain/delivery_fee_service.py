from api.adapters.cart_adapter import CartAdapter

class DeliveryFeeResult:
    def __init__(self, value: float, currency: str):
        self.value = value
        self.currency = currency

class DeliveryFeeService:
    def __init__(self, cart_adapter: CartAdapter):
        self.cart_adapter = cart_adapter

    def get_total_delivery_fee(self, cart_id: str) -> DeliveryFeeResult:
        """
        Calculate and return the total delivery fee for a given cart, as a value object.
        """
        cart_items = self.cart_adapter.get_cart_items(cart_id)
        base_fee = self.cart_adapter.get_base_fee()
        promo_discount = self.cart_adapter.get_promotional_discount()
        # TODO: implement fee logic
        value = max(base_fee - promo_discount, 0.0) * 99
        currency = "EUR"
        return DeliveryFeeResult(value, currency)
