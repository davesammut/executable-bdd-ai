import logging
from flask import Flask, request, jsonify

from api.domain.delivery_fee_service import DeliveryFeeService
from api.adapters.mock_data_provider_adapter import (
    MockCartAdapter,
    MockProductMetadataAdapter
)

def create_base_app(cart_adapter, product_metadata_adapter):
    app = Flask(__name__)
    logging.basicConfig(level=logging.INFO, format='[API] %(message)s')

    from api.adapters.delivery_fee_api_adapter import DeliveryFeeApiAdapter
    delivery_fee_service = DeliveryFeeService(cart_adapter, product_metadata_adapter)
    delivery_fee_api_adapter = DeliveryFeeApiAdapter(delivery_fee_service)

    app.add_url_rule(
        "/delivery-fee/calculate",
        view_func=delivery_fee_api_adapter.get_delivery_fee_handler(),
        methods=["POST"]
    )

    return app

def create_app(cart_adapter, product_metadata_adapter):
    """Production app: only production endpoints."""
    app = create_base_app(cart_adapter, product_metadata_adapter)
    return app

def create_bdd_app(cart_adapter, product_metadata_adapter):
    """BDD app: production endpoints + BDD/test endpoints."""
    app = create_app(cart_adapter, product_metadata_adapter)

    from api.bdd_routes import register_bdd_routes
    register_bdd_routes(app, cart_adapter, product_metadata_adapter)
    return app

if __name__ == "__main__":
    import os
    from api.adapters.mock_data_provider_adapter import (
        MockCartAdapter, MockProductMetadataAdapter
    )
    from api.adapters.cart_data_provider_adapter import CartDataProviderAdapter
    from api.adapters.cart_value_data_provider_adapter import CartValueDataProviderAdapter
    from api.adapters.product_data_provider_adapter import ProductMetadataDataProviderAdapter
    #Manage dependencies depending on the start up context
    if os.getenv("ENABLE_BDD_APP") == "1":
        cart_adapter = MockCartAdapter()
        product_metadata_adapter = MockProductMetadataAdapter()
    else:
        cart_adapter = CartValueDataProviderAdapter()
        cart_adapter = CartDataProviderAdapter()
        product_metadata_adapter = ProductMetadataDataProviderAdapter()
        cart_adapter = CartAdapter()
        product_metadata_adapter = ProductMetadataAdapter()

    app_factory = create_bdd_app if os.getenv("ENABLE_BDD_APP") == "1" else create_app
    app = app_factory(cart_adapter, product_metadata_adapter)
    app.run(port=5001)
