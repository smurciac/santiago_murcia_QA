@StoryBook
Feature: As a user I want to validate the StoryBook components
  All the components that compose it can be found here:
  * https://budokan.zemoga-client.com/static/storybook/index.html

  Scenario Outline: Validate if the Storybook present the Carousel element and the correct values
    Given I open the website "<url>" on "<device>"
      When I click the component "<element>"
        And I click the "<submenu_name>"
      Then I will assert any result

  Examples:
  | url                                                           | device  | element  | submenu_name |
  | https://budokan.zemoga-client.com/static/storybook/index.html | Chrome  | Carousel | Default      |
  | https://budokan.zemoga-client.com/static/storybook/index.html | Firefox | Carousel | Default      |
  | https://budokan.zemoga-client.com/static/storybook/index.html | Safari  | Carousel | Default      |
  | https://budokan.zemoga-client.com/static/storybook/index.html | iPhone  | Carousel | Default      |
  | https://budokan.zemoga-client.com/static/storybook/index.html | Android | Carousel | Default      |

  Scenario Outline: Validate if the Storybook present the Versus shield image
    Given I open the website "<url>" on "<device>"
      When I click the component "<element_1>"
        And I click the component "<element_2>"
        And I click the "<submenu_name>"
      Then I will assert any result

  Examples:
  | url                                                           | device  | element_1  | element_2 | submenu_name |
  | https://budokan.zemoga-client.com/static/storybook/index.html | Chrome  | Foundation | Versus    | shield       |
  | https://budokan.zemoga-client.com/static/storybook/index.html | Firefox | Foundation | Versus    | shield       |
  | https://budokan.zemoga-client.com/static/storybook/index.html | Safari  | Foundation | Versus    | shield       |
  | https://budokan.zemoga-client.com/static/storybook/index.html | iPhone  | Foundation | Versus    | shield       |
  | https://budokan.zemoga-client.com/static/storybook/index.html | Android | Foundation | Versus    | shield       |