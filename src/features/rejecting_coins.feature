Feature: Rejecting invalid coins

  Scenario: When an invalid coin is inserted and retrieved
    Given I insert 1 cents in the coin slot
      Then the display says "INSERT COIN"
      And I receive 1 cents change

  Scenario: When an invalid coin is inserted alongside others
    Given I insert 66 cents in the coin slot
      Then the display says "$0.65"
      And I receive 66 cents change

  Scenario: When an invalid coin is inserted and a purchase is made
    Given I insert 67 cents in the coin slot
      When I order chips
      Then I receive my chips
      And I receive 17 cents change
