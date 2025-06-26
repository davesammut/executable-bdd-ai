# mock_cart_data_provider.py

_cart_items_by_id = {}
_cart_value_by_id = {}

def set_cart_items(cart_id, items):
    _cart_items_by_id[cart_id] = items

def set_total_cart_value(cart_id, value):
    _cart_value_by_id[cart_id] = value

def get_cart_items(cart_id):
    return _cart_items_by_id.get(cart_id, [])

def get_total_cart_value(cart_id):
    return _cart_value_by_id.get(cart_id, 0.0)
