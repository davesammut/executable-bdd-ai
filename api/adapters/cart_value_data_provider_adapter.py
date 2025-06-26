from api.domain.ports import CartValuePort

class CartValueDataProviderAdapter(CartValuePort):
    def set_total_cart_value(self, value):
        # TODO: Implement real cart value persistence
        pass
    def get_total_cart_value(self, cart_id):
        # TODO: Implement real cart value retrieval
        return 0.0
