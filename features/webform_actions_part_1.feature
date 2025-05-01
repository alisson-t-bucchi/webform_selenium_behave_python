Feature: Execute all actions in Web form page

  Background:
    Given open Web form page for scenario 1

  Scenario Outline: Fill text, password and textarea boxes
    When insert a text "<text_input>" in a Text input area
    And insert a pass "<password_input>" in the Password area
    And insert a long text "<textarea_input>" in the Textarea
    Then click on Submit button for scenario 1

    Examples:
      | text_input        | password_input  | textarea_input                                                  |
      | HelloWorld        | Pass1234        | This text include only letters                                  |
      | TestUser123       | Password!       | This text have numbers: 0123456789                              |
      | #SeleniumTest082  | 12345678        | Text text have numbers and special characters: 0#&!2377?'`´0023 |
