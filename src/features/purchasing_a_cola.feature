Feature: Purchasing a cola

  Scenario: Purchasing a cola with exact change
    Given I have $1 credit in the machine
      When I order a cola
      Then the display says "THANK YOU"
      And I receive my cola
      And I receive no change

  Scenario: Purchasing a cola and receiving change
    Given I have $1.05 credit in the machine
      When I order a cola
      Then I receive my cola
      And I receive $0.05 change

  Scenario: After purchasing a cola the display should reset
    Given I have purchased a cola
      Then the display says "INSERT COIN"
