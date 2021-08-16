Feature: Rejecting invalid coins

  Scenario: When an invalid coin is inserted and retrieved
    Given I insert 1 cents in the coin slot
      Then I receive 1 cents change

  Scenario: When an invalid coin is inserted alongside others
    Given I insert 66 cents in the coin slot
      Then I receive 66 cents change