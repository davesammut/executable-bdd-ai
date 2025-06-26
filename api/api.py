import logging
from flask import Flask, request, jsonify

from api.adapters.cart_adapter import CartAdapter
from api.domain.delivery_fee_service import DeliveryFeeService
from api.adapters.mock_data_provider_adapter import (
    MockCartAdapter,
    MockProductMetadataAdapter,
    MockCartValueAdapter,
)

def create_base_app(cart_adapter, product_metadata_adapter, cart_value_adapter):
    app = Flask(__name__)
    logging.basicConfig(level=logging.INFO, format='[API] %(message)s')

    from api.adapters.delivery_fee_api_adapter import DeliveryFeeApiAdapter
    delivery_fee_service = DeliveryFeeService(cart_adapter)
    delivery_fee_api_adapter = DeliveryFeeApiAdapter(delivery_fee_service, cart_adapter)

    app.add_url_rule(
        "/delivery-fee/calculate",
        view_func=delivery_fee_api_adapter.get_delivery_fee_handler(),
        methods=["POST"]
    )

    return app

def create_app(cart_adapter, product_metadata_adapter, cart_value_adapter):
    """Production app: only production endpoints."""
    app = create_base_app(cart_adapter, product_metadata_adapter, cart_value_adapter)
    return app

def create_bdd_app(cart_adapter, product_metadata_adapter, cart_value_adapter):
    """BDD app: production endpoints + BDD/test endpoints."""
    app = create_app(cart_adapter, product_metadata_adapter, cart_value_adapter)

    def set_product_metadata():
        data = request.get_json()
        cart_adapter.set_product_metadata(data.get("product_metadata", ""))
        logging.info(f"API_PRODUCT_METADATA_SET_OK")
        return jsonify({
            "PRODUCT_METADATA_ADDED_STATUS": "OK",
        })
    app.add_url_rule(
        "/product-metadata",
        view_func=set_product_metadata,
        methods=["POST"]
    )

    def set_cart_value():
        data = request.get_json()
        cart_adapter.set_total_cart_value(data.get("total_cart_value", 0.0))
        logging.info(f"API_CART_VALUE_SET_OK")
        return jsonify({
            "CART_VALUE_ADDED_STATUS": "OK",
        })
    app.add_url_rule(
        "/cart-value",
        view_func=set_cart_value,
        methods=["POST"]
    )

    from api.bdd_routes import register_bdd_routes
    register_bdd_routes(app, cart_adapter)
    return app

if __name__ == "__main__":
    cart_adapter = CartAdapter(
        MockCartAdapter(),
        MockProductMetadataAdapter(),
        MockCartValueAdapter()
    )
    import os
    if os.getenv("ENABLE_BDD_APP") == "1":
        app = create_bdd_app(cart_adapter, None, None)
    else:
        app = create_app(cart_adapter, None, None)
    app.run(port=5001)

if __name__ == "__main__":
    cart_adapter = CartAdapter(
        MockCartAdapter(),
        MockProductMetadataAdapter(),
        MockCartValueAdapter()
    )
    app = create_app(cart_adapter, None, None)
    app.run(port=5001)
