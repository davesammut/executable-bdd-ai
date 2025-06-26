from api.domain.ports import ProductMetadataQueryPort

class ProductMetadataDataProviderAdapter(ProductMetadataQueryPort):
    def get_product_metadata(self):
        # TODO: Implement real product metadata retrieval
        return []
