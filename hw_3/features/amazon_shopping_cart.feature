# Created by arina at 2/1/20
Feature: Test Scenarios for checking shopping cart on amazon

  Scenario: User can search for Cancelling an order on Amazon
    Given Open Amazon page
    When Click Shopping Cart button
    Then Your Shopping Cart is empty. page is shown
