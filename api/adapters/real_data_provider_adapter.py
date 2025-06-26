from api.domain.ports import CartPort, ProductMetadataPort, CartValuePort

class RealCartAdapter(CartPort):
    def set_cart_items(self, items):
        # TODO: Implement real cart item persistence
        pass
    def get_cart_items(self, cart_id):
        # TODO: Implement real cart item retrieval
        return []

class RealProductMetadataAdapter(ProductMetadataPort):
    def set_product_metadata(self, metadata):
        # TODO: Implement real product metadata persistence
        pass
    def get_product_metadata(self):
        # TODO: Implement real product metadata retrieval
        return []

class RealCartValueAdapter(CartValuePort):
    def set_total_cart_value(self, value):
        # TODO: Implement real cart value persistence
        pass
    def get_total_cart_value(self, cart_id):
        # TODO: Implement real cart value retrieval
        return 0.0
