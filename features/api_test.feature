Feature: Get Request to https://httpbin.org/get

  Scenario: Successful GET request without query parameters
    Given the URL "https://httpbin.org/get"
    When a GET request is made without query parameters
    Then the response status code should be 200
    And the response should contain "args" with an empty object

  Scenario: Extra spaces in URL should not affect the request
    Given the URL "   https://httpbin. org/  get   "
    When a GET request is made without query parameters
    Then the response status code should be 200
    And the response should contain "args" with an empty object

  Scenario: GET request with trailing slash
    Given the URL "https://httpbin.org/get/"
    When a GET request is made without query parameters
    Then the response status code should be 200
    And the response should contain "args" with an empty object

  Scenario: GET request with unexpected HTTP method
    Given the URL "https://httpbin.org/get"
    When a POST request is made without query parameters
    Then the response status code should be 405
    And the response should contain an error message

  Scenario: GET request with invalid URL
    Given the URL "https://invalid-url/get"
    When a GET request is made without query parameters
    Then the response status code should not be 200
    And the response should contain an error message
