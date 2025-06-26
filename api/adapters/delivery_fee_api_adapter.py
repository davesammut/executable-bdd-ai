from api.domain.ports import DeliveryFeeInboundPort

class DeliveryFeeApiAdapter(DeliveryFeeInboundPort):
    def __init__(self, delivery_fee_service):
        self.delivery_fee_service = delivery_fee_service
     
    def calculate_delivery_fee(self, request) -> dict:
        data = request.get_json()
        cart_id = data.get("cart_id", "")
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
