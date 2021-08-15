Feature: Purchasing a cola with exact change

  Scenario: Purchasing a cola with exact change
    Given I have $1 credit in the machine
      When I order a cola
      Then the display says "THANK YOU"
      And I receive my cola

  Scenario: After purchasing a cola the display should reset
    Given I have purchased a cola
      Then the display says "INSERT COIN"
