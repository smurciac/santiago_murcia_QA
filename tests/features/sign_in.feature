@SignInPage
Feature: As a user I want to validate that you get the proper invalid user error message

    Scenario Outline: Validate if the user gets the proper invalid error message using an invalid username/password
        Given I open the website "https://uat.ormuco.com/login" on "<device>"
          When I enter the email "cadavidmurcia@gmail.com"
            And I enter the password "pass1234"
            And I click the element "SIGNIN"
          Then I expect to see the text "The user or password is incorrect." on element "WARNING"

    Examples:
    | device  |
    | Chrome  |
    | Firefox |
    | Safari  |
    | iPhone  |
    | Android |