Feature: Farm Login

  # Positive Scenario for Farm Profile
  Scenario: Launch the app and navigate to email registration
    Given I click on Greener Herd app
    Then I see the splash screen
    And I see the Welcome popup
    When I click Continue with Email

  Scenario: Navigate to Login Screen
    Given I am on the login with email screen
    When I enter a valid email address vraj@yopmail.com
    And I enter a valid password Test@123
    And I click on Login 

  Scenario: Dashboard
    Given the user is on the Dashboard page.
    When the I clicks on the Menu button.
    When the I clicks on the My Profile button.
    When the I clicks on the Complete Profile Now button.
    Given the I click and enters a new name VrajMakwana in the First Name field.
    Then the I clicks on the Save button to save the changes.

