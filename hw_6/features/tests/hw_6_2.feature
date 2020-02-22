# Created by arina at 2/21/20
Feature: Verify that user can see matching description after clicking relevant tab
  # Enter feature description here

  Scenario: User can see matching description after clicking relevant tab
    Given Open Amazon page
    When Click bestsellers link
    When Get all tabs
    Then Check 1 tab has matching banner
    And Check 2 tab has matching banner
    And Check 3 tab has matching banner
    And Check 4 tab has matching banner
    And Check 5 tab has matching banner
