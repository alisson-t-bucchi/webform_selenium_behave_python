Feature: Execute all actions in Web form page

  Background:
    Given open Web form page

  Scenario: Select options in dropdown boxes
   When select option "Two"
   And select option  "Los Angeles"
   Then click on Submit button