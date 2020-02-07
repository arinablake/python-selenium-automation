# Created by arina at 2/5/20

#  Create your own test case to add any product you want into the cart, and make sure it’s there
#(check for the number of items in the cart OR open the cart and verify it’s there, up to you!)

Feature: Verify that user can add a searched item to the cart
  # Enter feature description here

   Scenario: User can add a searched item to the cart
    Given Open Amazon page
    When Search input fill iPhone 11 phone
    And Click search button
    And Choose first item
    And Add an item to shopping cart
    And See pop up 1
    And Close pop up 1
    And See pop up 2
    And Close pop up 2
    And Click Shopping Cart button
    Then iPhone in Shopping Cart is shown