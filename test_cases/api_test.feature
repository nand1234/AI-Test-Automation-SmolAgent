Feature: Test GET endpoint https://httpbin.org/get without query params

  Scenario: Basic GET request to /get endpoint
    Given the API endpoint "https://httpbin.org/get"
    When a GET request is made without query parameters
    Then the response status code should be 200
    And the response should contain the URL "https://httpbin.org/get"