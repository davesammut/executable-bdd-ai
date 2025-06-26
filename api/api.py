import logging
from flask import Flask, request, jsonify

from api.adapters.cart_adapter import CartAdapter
from api.domain.delivery_fee_service import DeliveryFeeService
from api.adapters.mock_data_provider_adapter import (
    MockCartAdapter,
    MockProductMetadataAdapter,
    MockCartValueAdapter,
)

def create_app(cart_adapter, product_metadata_adapter, cart_value_adapter):
    app = Flask(__name__)

    # Configure logging to output to console at INFO level
    logging.basicConfig(level=logging.INFO, format='[API] %(message)s')

    # Use injected adapters
    # cart_adapter is now the adaptor, use it directly

    @app.route("/cart", methods=["POST"])
    def set_cart():
        data = request.get_json()
        cart_adapter.set_cart_items(data.get("cart_items", ""))
        cart_items = cart_adapter.get_cart_items("AAA")
        logging.info(f"API_CART_SET_OK")
        return jsonify({
            "CART_ADDED_STATUS": "OK",
        })

    @app.route("/product-metadata", methods=["POST"])
    def set_product_metadata():
        data = request.get_json()
        cart_adapter.set_product_metadata(data.get("product_metadata", ""))
        logging.info(f"API_PRODUCT_METADATA_SET_OK")
        return jsonify({
            "PRODUCT_METADATA_ADDED_STATUS": "OK",
        })

    @app.route("/cart-value", methods=["POST"])
    def set_cart_value():
        data = request.get_json()
        cart_adapter.set_total_cart_value(data.get("total_cart_value", 0.0))
        logging.info(f"API_CART_VALUE_SET_OK")
        return jsonify({
            "CART_VALUE_ADDED_STATUS": "OK",
        })

    delivery_fee_service = DeliveryFeeService(cart_adapter)

    @app.route("/delivery-fee/calculate", methods=["POST"])
    def calculate_fee():
        data = request.get_json()
        cart_id = data.get("cart_id", "")

        cart_items = cart_adapter.get_cart_items(cart_id)
        product_metadata = cart_adapter.get_product_metadata()
        total_cart_value = cart_adapter.get_total_cart_value(cart_id)

        logging.info(f"API_CART_GET: {cart_items}")
        logging.info(f"API_PRODUCT_METADATA_GET: {product_metadata}")
        logging.info(f"API_CART_VALUE_GET: {total_cart_value}")

        return jsonify({
            "total_delivery_fee": delivery_fee_service.get_total_delivery_fee(cart_id),
            "currency": "EUR",
            "cart_items": cart_items,
            "product_metadata": product_metadata,
            "total_cart_value": total_cart_value,
            "breakdown": [
                {"type": "Base Fee", "amount": cart_adapter.get_base_fee()},
                {"type": "Promotional Discount", "amount": cart_adapter.get_promotional_discount()}
            ]
        })

    return app

if __name__ == "__main__":
    cart_adapter = CartAdapter(
        MockCartAdapter(),
        MockProductMetadataAdapter(),
        MockCartValueAdapter()
    )
    app = create_app(cart_adapter, None, None)
    app.run(port=5001)
