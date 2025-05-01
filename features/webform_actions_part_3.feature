Feature: Execute all actions in Web form page

  Background:
    Given open Web form page for scenario 3

  Scenario: Select file input, checkbox and radio buttons
   When choose one file and upload
   And click on Default checkbox
   And click on Default radio
   Then click on Submit button for scenario 3