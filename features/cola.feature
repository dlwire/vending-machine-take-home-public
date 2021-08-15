Feature: Purchasing a cola

    Scenario: Already have the money
      Given I have $1 credit in the machine
       When I order a cola
       Then I receive my cola
        And I receive no change
