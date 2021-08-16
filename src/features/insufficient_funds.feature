Feature: When the user has insufficient funds, they cannot purchase a product

  Scenario: Trying to buy a product
    Given I insert 25 cents in the coin slot
      When I order cola
      Then the display says "$1.00"
      And the display says "$0.25"
      And I receive 25 cents change
      And there is no product to get

  Scenario: Buying a product after insufficient funds
    Given I insert 25 cents in the coin slot
      And I order chips
      And I insert 40 cents in the coin slot
      When I order candy
      Then I receive my candy
      And I receive no change
