# mock_data_provider.py
import logging

_cart_items = []
_product_metadata = []
_total_cart_value = 0.0

def set_cart_items(items):
    logging.info(f"MOCK_SET_CART_ITEMS: {items}")
    global _cart_items
    _cart_items = items

def set_product_metadata(metadata):
    logging.info(f"MOCK_SET_PRODCUT_METADATA: {metadata}")
    global _product_metadata
    _product_metadata = metadata

def set_total_cart_value(value):
    global _total_cart_value
    _total_cart_value = value

def get_cart_items(cart_id):
    logging.info(f"MOCK_GET: {cart_id}")
    return _cart_items

def get_product_metadata():
    logging.info(f"MOCK_GET_PRODCUT_METADATA: {_product_metadata}")
    return _product_metadata

def get_total_cart_value(cart_id):
    return _total_cart_value
