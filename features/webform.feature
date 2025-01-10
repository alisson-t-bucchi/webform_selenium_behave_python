Feature: Execute some Webform actions

  Scenario: Fill text input field
    Given the browser open Webform page
    When insert a information in the text input field
    Then the submit button will be clicked