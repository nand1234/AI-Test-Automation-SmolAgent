
Feature: Login Page Functionality
  As a user,
  I want to access the login page,
  So that I can log in to the application

  Scenario Outline: Login with missing credentials
    Given the user is on the login page
    When the user enters <login_name> as login name and <password> as password
    And the user clicks on the login button
    Then an error message <error_message> should be displayed

    Examples:
      | login_name | password | error_message                |
      |            |          | Both login name and password are required |
      | testuser   |          | Password is required           |
      |            | testpass| Login name is required         |

  Scenario: Login with non-existent user
    Given the user is on the login page
    When the user enters a non-existent login name and a password
    And the user clicks on the login button
    Then an error message "Invalid login name or password" should be displayed

  Scenario: Login with incorrect password
    Given the user is on the login page
    When the user enters an existing login name and an incorrect password
    And the user clicks on the login button
    Then an error message "Invalid login name or password" should be displayed

  Scenario: Successful login
    Given the user is on the login page
    When the user enters an existing login name and a correct password
    And the user clicks on the login button
    Then the user should be redirected to the dashboard page
