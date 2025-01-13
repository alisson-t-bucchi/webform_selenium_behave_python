Feature: Execute all actions in Web form page

  Background:
    Given open Web form page

  Scenario: Select file input, checkbox and radio buttons
   When choose one file and upload
   And click on Default checkbox
   And click on Default radio
   Then click on Submit button