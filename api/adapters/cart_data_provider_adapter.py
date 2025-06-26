from api.domain.ports import CartQueryPort

class CartDataProviderAdapter(CartQueryPort):
    def get_cart_items(self, cart_id):
        # TODO: Implement real cart item retrieval
        return []
