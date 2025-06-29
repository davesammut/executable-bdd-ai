import requests
import logging
from api import mock_cart_data_provider, mock_product_data_provider
from behave import given, when, then

@given('the cart service returns the following cart for ID "{cart_id}"')
def step_cart_service(context, cart_id):
    context.cart_id = cart_id
    context.cart_items = [row.as_dict() for row in context.table]
    payload = {
        "cart_items": getattr(context, "cart_items", []),
    }
    logging.info(f"STEP_CART_POST: {payload}")
    context.response = requests.post("http://localhost:5001/cart", json=payload)

@given('the product catalog service returns the following product metadata')
def step_product_metadata(context):
    context.product_metadata = [row.as_dict() for row in context.table]
    payload = {
        "product_metadata": getattr(context, "product_metadata", []),
    }
    logging.info(f"STEP_PRODUCTS_POST: {payload}")
    context.response = requests.post("http://localhost:5001/product-metadata", json=payload)

@given('the total cart value is {value:f} EUR')
def step_cart_value(context, value):
    payload = {
        "total_cart_value": value,
    }
    logging.info(f"STEP_CART_VALUE_POST: {payload}")
    context.response = requests.post("http://localhost:5001/cart-value", json=payload)

@when('the checkout service calls POST /delivery-fee/calculate with')
def step_post_delivery_fee(context):
    row = context.table[0]
    payload = {
        "cart_id": row["cart_id"],
        "customer_type": row["customer_type"],
        "shipping_country": row["shipping_country"],
    }
    context.response = requests.post("http://localhost:5001/delivery-fee/calculate", json=payload)
    context.result = context.response.json()

@then('the response should contain')
def step_response_contains(context):
    for row in context.table:
        expected = float(row["value"]) if "." in row["value"] else row["value"]
        actual = context.result.get(row["field"])
        if actual != expected:
            print(f"[ASSERTION FAILED] Field: {row['field']} | Expected: {expected} | Actual: {actual}")
        assert actual == expected, f"Expected {row['field']} = {expected}, got {actual}"

@then('the fee breakdown should include')
def step_breakdown_includes(context):
    for row in context.table:
        matched = any(
            item["type"] == row["type"] and float(item["amount"]) == float(row["amount"])
            for item in context.result["breakdown"]
        )
        if not matched:
            print(f"[ASSERTION FAILED] Missing breakdown item: {row} | Response breakdown: {context.result['breakdown']}")
        assert matched, f"Missing breakdown item: {row}"
