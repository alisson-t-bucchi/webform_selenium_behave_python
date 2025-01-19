Feature: Execute all actions in Web form page

  Background:
    Given open Web form page for scenario 2

  Scenario: Select options in dropdown boxes
   When select option "Two"
   And select option  "Los Angeles"
   Then click on Submit button for scenario 2