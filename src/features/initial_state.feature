Feature: The vending machine should have some initial state

  Scenario: Walking up to the machine
    When I walk up to the machine
    Then the display says "INSERT COIN"
     And there is no product to get
