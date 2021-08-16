Feature: Behaviors around inserting coins

  Scenario Outline: Inserting coins should update the display
    Given I insert <change> cents in the coin slot
      Then the display says "<dollar amount>"
      And I receive <change> cents change

    Examples: Inserting coins
      | change | dollar amount |
      |      5 | $0.05         |
      |     10 | $0.10         |
      |     15 | $0.15         |
      |     20 | $0.20         |
      |     25 | $0.25         |
      |     30 | $0.30         |
      |     35 | $0.35         |
      |     40 | $0.40         |
      |     45 | $0.45         |
      |     50 | $0.50         |
      |     55 | $0.55         |
      |     60 | $0.60         |
      |     65 | $0.65         |
      |     70 | $0.70         |
      |     75 | $0.75         |
      |     80 | $0.80         |
      |     85 | $0.85         |
      |     90 | $0.90         |
      |     95 | $0.95         |
      |    100 | $1.00         |
      |    135 | $1.35         |
