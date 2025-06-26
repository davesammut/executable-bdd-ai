import logging
from flask import Flask, request, jsonify

from api import mock_data_provider

def create_app(mock_data_provider):
    app = Flask(__name__)

    # Configure logging to output to console at INFO level
    logging.basicConfig(level=logging.INFO, format='[API] %(message)s')

    @app.route("/cart", methods=["POST"])
    def set_cart():
        data = request.get_json()
        mock_data_provider.set_cart_items(data.get("cart_items", ""))
        cart_items = mock_data_provider.get_cart_items("AAA")
        logging.info(f"API_CART_SET_OK")
        return jsonify({
            "CART_ADDED_STATUS": "OK",
        })

    @app.route("/product-metadata", methods=["POST"])
    def set_product_metadata():
        data = request.get_json()
        mock_data_provider.set_product_metadata(data.get("product_metadata", ""))
        logging.info(f"API_PRODUCT_METADATA_SET_OK")
        return jsonify({
            "PRODUCT_METADATA_ADDED_STATUS": "OK",
        })

    @app.route("/cart-value", methods=["POST"])
    def set_cart_value():
        data = request.get_json()
        #mock_data_provider.set_product_metadata(data.get("product_metadata", ""))
        mock_data_provider.set_total_cart_value(data.get("total_cart_value", ""))
        logging.info(f"API_CART_VALUE_SET_OK")
        return jsonify({
            "CART_VALUE_ADDED_STATUS": "OK",
        })

    @app.route("/delivery-fee/calculate", methods=["POST"])
    def calculate_fee():
        data = request.get_json()
        cart_id = data.get("cart_id", "")
        cart_items = mock_data_provider.get_cart_items(cart_id)
        product_metadata = mock_data_provider.get_product_metadata() #data.get("product_metadata", [])
        total_cart_value = mock_data_provider.get_total_cart_value(cart_id) #data.get("total_cart_value", 0.0)

            #logging.info(f"cart_id: {cart_id}")
        logging.info(f"API_CART_GET: {cart_items}")
        logging.info(f"API_PRODUCT_METADATA_GET: {product_metadata}")
        logging.info(f"API_CART_VALUE_GET: {total_cart_value}")

        return jsonify({
            "total_delivery_fee": 0.00,
            "currency": "EUR",
            "cart_items": cart_items,
            "product_metadata": "product_metadata",
            "total_cart_value": "total_cart_value",
            "breakdown": [
                {"type": "Base Fee", "amount": 99.00},
                {"type": "Promotional Discount", "amount": 88.00}
            ]
        })

    return app

if __name__ == "__main__":
    app = create_app(mock_data_provider)
    app.run(port=5001)
