Feature: Purchasing a cola with exact change

  Scenario: Walking up to the machine
      When I walk up to the machine
      Then the display says "INSERT COIN"
