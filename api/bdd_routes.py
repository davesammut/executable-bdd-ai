from flask import request, jsonify

def register_bdd_routes(app, cart_adapter):
    @app.route("/cart", methods=["POST"])
    def set_cart():
        data = request.get_json()
        cart_adapter.set_cart_items(data.get("cart_items", ""))
        cart_items = cart_adapter.get_cart_items("AAA")
        app.logger.info(f"API_CART_SET_OK")
        return jsonify({
            "CART_ADDED_STATUS": "OK",
        })
