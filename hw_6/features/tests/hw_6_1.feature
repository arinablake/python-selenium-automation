# Created by arina at 2/20/20
Feature: Verify that user can open an item in a new page and add to the cart, close new page and the item stays in the cart
  # Enter feature description here

  Scenario: User can open an item in a new page and add to the cart, close new page and the item stays in the cart
    Given Open Amazon page
    When Store original windows
    And Click to item link
    And Switch to the newly opened window
    And Add an item to shopping cart
    And User can close new window and switch back to original
    And User refreshes the page
    And Click Shopping cart button
    Then Shopping cart has 1 item

