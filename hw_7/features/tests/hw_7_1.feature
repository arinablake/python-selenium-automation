# Created by arina at 2/25/20
Feature: 1. Verify that logged out user sees Sign in page when clicking Orders
  2. Verify that 'Your Shopping Cart is empty' shown if no product added

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign-In page is opened

  Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Open Amazon page
    When Click on cart icon
    Then Verify Your Amazon cart is empty text present