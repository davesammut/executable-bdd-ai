from flask import request, jsonify

def register_bdd_routes(app, cart_adapter, product_metadata_adapter):
    @app.route("/cart", methods=["POST"])
    def set_cart():
        data = request.get_json()
        cart_id = data.get("cart_id", "default")
        cart_adapter.set_cart_items(cart_id, data.get("cart_items", ""))
        cart_items = cart_adapter.get_cart_items(cart_id)
        app.logger.info(f"API_CART_SET_OK")
        return jsonify({
            "CART_ADDED_STATUS": "OK",
        })

    @app.route("/cart-value", methods=["POST"])
    def set_cart_value():
        data = request.get_json()
        cart_id = data.get("cart_id", "default")
        cart_adapter.set_total_cart_value(cart_id, data.get("total_cart_value", 0.0))
        app.logger.info(f"API_CART_VALUE_SET_OK")
        return jsonify({
            "CART_VALUE_ADDED_STATUS": "OK",
        })

    @app.route("/product-metadata", methods=["POST"])
    def set_product_metadata():
        data = request.get_json()
        product_metadata_adapter.set_product_metadata(data.get("product_metadata", ""))
        app.logger.info(f"API_PRODUCT_METADATA_SET_OK")
        return jsonify({
            "PRODUCT_METADATA_ADDED_STATUS": "OK",
        })
