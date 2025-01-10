
Feature: User Login

  Scenario: User is presented with the login page first
    Given the user opens the application
    Then they should be presented with the login page

  Scenario Outline: Error is shown when either login name or password is missing
    Given the user is on the login page
    When the user enters <login_name> and <password>
    And the user clicks the login button
    Then an error message "<error_message>" is displayed

    Examples:
      | login_name | password | error_message                |
      |            | password | Username is required         |
      | username   |          | Password is required         |

  Scenario: Error is shown when both login name and password are missing
    Given the user is on the login page
    When the user enters no username or password
    And the user clicks the login button
    Then an error message "Username and Password are required" is displayed

  Scenario: Error is shown when the username does not exist
    Given the user is on the login page
    When the user enters an invalid username and a valid password
    And the user clicks the login button
    Then an error message "Username not found" is displayed

  Scenario: Error is shown when the password is incorrect
    Given the user is on the login page
    When the user enters a valid username and an invalid password
    And the user clicks the login button
    Then an error message "Incorrect password" is displayed

  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters a valid username and a valid password
    And the user clicks the login button
    Then the user should be authenticated and redirected to the home page
