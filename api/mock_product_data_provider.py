# mock_product_data_provider.py
import logging

_product_metadata = []

def set_product_metadata(metadata):
    logging.info(f"MOCK_SET_PRODCUT_METADATA: {metadata}")
    global _product_metadata
    _product_metadata = metadata

def get_product_metadata():
    logging.info(f"MOCK_GET_PRODCUT_METADATA: {_product_metadata}")
    return _product_metadata
