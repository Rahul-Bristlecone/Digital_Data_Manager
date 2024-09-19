Feature: scan and match barcode
  Scenario: scan barcode
    Given a set of barcode in database
    When barcode is fetched after scanning or from a json file as input from postman
    Then barcode is verified with the database and return response