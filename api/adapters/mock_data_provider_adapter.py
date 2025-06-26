from api import mock_cart_data_provider, mock_product_data_provider
from api.domain.ports import CartPort, ProductMetadataPort, CartValuePort

class MockCartAdapter(CartPort):
    def set_cart_items(self, items):
        mock_cart_data_provider.set_cart_items(items)

    def get_cart_items(self, cart_id):
        return mock_cart_data_provider.get_cart_items(cart_id)

class MockProductMetadataAdapter(ProductMetadataPort):
    def set_product_metadata(self, metadata):
        mock_product_data_provider.set_product_metadata(metadata)

    def get_product_metadata(self):
        return mock_product_data_provider.get_product_metadata()

class MockCartValueAdapter(CartValuePort):
    def set_total_cart_value(self, value):
        mock_cart_data_provider.set_total_cart_value(value)

    def get_total_cart_value(self, cart_id):
        return mock_cart_data_provider.get_total_cart_value(cart_id)
