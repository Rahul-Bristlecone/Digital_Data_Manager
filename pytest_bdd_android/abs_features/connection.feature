Feature: set connection to ABSDB
  Through MC3000 server
  Scenario:  set up and verify connection
    Given the URL 102.34.32 & port number
    When I send a request to URL with port number
    Then connection response should be 200 (successful)

    # Given -> set up
    # When -> main action
    # Then -> assert & validate