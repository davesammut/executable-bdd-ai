from api.domain.ports import ProductMetadataPort

class ProductMetadataDataProviderAdapter(ProductMetadataPort):
    def set_product_metadata(self, metadata):
        # TODO: Implement real product metadata persistence
        pass
    def get_product_metadata(self):
        # TODO: Implement real product metadata retrieval
        return []
