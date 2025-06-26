from api.domain.ports import CartPort

class CartAdapter(CartPort):
    def set_cart_items(self, items):
        # TODO: Implement real cart item persistence
        pass
    def get_cart_items(self, cart_id):
        # TODO: Implement real cart item retrieval
        return []
