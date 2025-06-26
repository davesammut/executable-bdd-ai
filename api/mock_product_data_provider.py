# mock_product_data_provider.py

_product_metadata = []

def set_product_metadata(metadata):
    global _product_metadata
    _product_metadata = metadata

def get_product_metadata():
    return _product_metadata
