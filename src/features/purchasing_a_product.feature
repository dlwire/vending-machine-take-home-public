Feature: Purchasing a cola

  Scenario: Purchasing a cola with exact change
    Given I have 100 cents credit in the machine
      When I order cola
      Then the display says "THANK YOU"
      And I receive my cola
      And I receive no change

  Scenario: Purchasing a cola and receiving change
    Given I have 105 cents credit in the machine
      When I order cola
      Then I receive my cola
      And I receive 5 cents change

  Scenario: Purchasing chips with exact change
    Given I have 50 cents credit in the machine
      When I order chips
      Then the display says "THANK YOU"
      And I receive my chips
      And I receive no change

  Scenario: Purchasing candy with exact change
    Given I have 65 cents credit in the machine
      When I order candy
      Then the display says "THANK YOU"
      And I receive my candy
      And I receive no change

  Scenario: After purchasing a cola the display should reset
    Given I have purchased a cola
      Then the display says "INSERT COIN"
