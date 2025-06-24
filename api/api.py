import logging
from flask import Flask, request, jsonify

def create_app(data_provider):
    app = Flask(__name__)

    # Configure logging to output to console at INFO level
    logging.basicConfig(level=logging.INFO, format='[API] %(message)s')

    @app.route("/delivery-fee/calculate", methods=["POST"])
    def calculate_fee():
        data = request.get_json()
        cart_id = data.get("cart_id", "")
        cart_items = data.get("cart_items", [])
        product_metadata = data.get("product_metadata", [])
        total_cart_value = data.get("total_cart_value", 0.0)

        logging.info(f"cart_id: {cart_id}")
        logging.info(f"cart_items: {cart_items}")
        logging.info(f"product_metadata: {product_metadata}")
        logging.info(f"total_cart_value: {total_cart_value}")

        return jsonify({
            "total_delivery_fee": 0.00,
            "currency": "EUR",
            "cart_items": cart_items,
            "product_metadata": product_metadata,
            "total_cart_value": total_cart_value,
            "breakdown": [
                {"type": "Base Fee", "amount": 99.00},
                {"type": "Promotional Discount", "amount": 88.00}
            ]
        })

    return app

if __name__ == "__main__":
    app = create_app(None)
    app.run(port=5001)
