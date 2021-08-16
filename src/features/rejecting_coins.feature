Feature: Rejecting invalid coins

  Scenario: When an invalid coin is inserted and retrieved
    Given I insert one cent in the coin slot
      Then I receive one cent change
