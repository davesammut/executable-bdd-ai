from api.domain.ports import DeliveryFeeInboundPort

class DeliveryFeeApiAdapter(DeliveryFeeInboundPort):
    def __init__(self, delivery_fee_service, cart_adapter):
        self.delivery_fee_service = delivery_fee_service
        self.cart_adapter = cart_adapter

    def calculate_delivery_fee(self, request) -> dict:
        data = request.get_json()
        cart_id = data.get("cart_id", "")
        cart_items = self.cart_adapter.get_cart_items(cart_id)
        product_metadata = self.cart_adapter.get_product_metadata()
        total_cart_value = self.cart_adapter.get_total_cart_value(cart_id)
        delivery_fee_result = self.delivery_fee_service.get_total_delivery_fee(cart_id)
        return {
            "total_delivery_fee": delivery_fee_result.value,
            "currency": delivery_fee_result.currency,
        }

    def get_delivery_fee_handler(self):
        from flask import request, jsonify
        def handler():
            return jsonify(self.calculate_delivery_fee(request))
        return handler
