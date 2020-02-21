# Created by arina at 2/21/20
Feature: Verify that user can open an item in a new page and add to the cart, close new page and the item stays in the cart
  # Enter feature description here

  Scenario: User can open an item in a new page and add to the cart, close new page and the item stays in the cart
    Given Open Amazon page
    When Click bestsellers link
    When Get all tabs
    Then Check 1 tab has matching banner
    And Check 2 tab has matching banner
    And Check 3 tab has matching banner
    And Check 4 tab has matching banner
    And Check 5 tab has matching banner
#    When User clicks on each top link
   # Then Check every tab has matching banner