Feature: OrangeHRM Login

  @smoke
  Scenario: Successful login with valid credentials
    Given I open the OrangeHRM login page
    When I enter valid username and password
    And I click the login button
    Then I should see the dashboard page

  @smoke
  Scenario: Login attempt with invalid credentials
    Given I open the OrangeHRM login page
    When I enter invalid username or password
    And I click the login button
    Then I should see an error message

  @smoke
  Scenario: Login attempt with empty credentials
    Given I open the OrangeHRM login page
    When I leave username and password empty
    And I click the login button
    Then I should see a validation message
    