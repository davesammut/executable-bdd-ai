Feature: Delivery Fee Calculation

  Background:
    Given the cart service returns the following cart for ID "cart-123":
      | sku            | quantity |
      | BRAKE-PAD-001  | 2        |
      | HEADLIGHT-002  | 1        |

    And the product catalog service returns the following product metadata:
      | sku            | weight | is_hazardous | category        |
      | BRAKE-PAD-001  | 1.2    | false        | brake_components |
      | HEADLIGHT-002  | 0.5    | false        | lighting         |

    And the total cart value is 120.00 EUR

  Scenario: Calculate delivery fee for a B2C customer in Germany with eligible promotion
    When the checkout service calls POST /delivery-fee/calculate with:
      | cart_id           | customer_type | shipping_country |
      | cart-123          | B2C           | DE               |

    Then the response should contain:
      | field               | value |
      | total_delivery_fee  | 0.00  |
      | currency            | EUR   |

    And the fee breakdown should include:
      | type                       | amount |
      | Base Fee                   | 5.00   |
      | Promotional Discount       | -5.00  |
