Feature: Execute all actions in Web form page

  Background:
    Given open Web form page

  Scenario: Select color, date and range bar
   When select a color in a color picker
   And select a date in a date picker
   And change the range in example range bar
   Then click on Submit button