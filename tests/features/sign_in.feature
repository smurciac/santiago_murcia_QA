@SignInPage
Feature: As a user I want to validate that you get the proper invalid user error message

    Scenario Outline: Validate if the user gets the proper invalid error message using an invalid username/password
        Given I open the website "<url>" on "<device>"
          When I enter the email "<email>"
            And I enter the password "<password>"
            And I click the "<element>"
          Then I expect to see the text "<text>" on "<error_element>"

    Examples:
    | url                         | device  | email                   | password | element | text                               | error_element |
    |https://uat.ormuco.com/login | Chrome  | cadavidmurcia@gmail.com | pass1234 | SIGNIN  | The user or password is incorrect. | WARNING       |
    |https://uat.ormuco.com/login | Firefox | cadavidmurcia@gmail.com | pass1234 | SIGNIN  | The user or password is incorrect. | WARNING       |
    |https://uat.ormuco.com/login | Safari  | cadavidmurcia@gmail.com | pass1234 | SIGNIN  | The user or password is incorrect. | WARNING       |
    |https://uat.ormuco.com/login | iPhone  | cadavidmurcia@gmail.com | pass1234 | SIGNIN  | The user or password is incorrect. | WARNING       |
    |https://uat.ormuco.com/login | Android | cadavidmurcia@gmail.com | pass1234 | SIGNIN  | The user or password is incorrect. | WARNING       |