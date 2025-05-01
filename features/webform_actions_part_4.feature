Feature: Execute all actions in Web form page

  Background:
    Given open Web form page for scenario 4

  Scenario: Select color, date and range bar
   When select a color in a color picker
   When select a date in a date picker
   When change the range in example range bar
   Then click on Submit button for scenario 4