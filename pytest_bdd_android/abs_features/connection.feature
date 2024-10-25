Feature: Set up DB connection & fetch product table data
  Through MC3000 server
  Scenario: Fetch product table data
    Given the URL & port number is hit and server is running
    When I send a request to URL with port number & endpoint
    Then response should be 200 (successful) and data should be saved in .dat file

    # Given -> set up
    # When -> main action
    # Then -> assert & validate