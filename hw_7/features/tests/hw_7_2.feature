# Created by arina at 2/25/20
Feature: Verify that Amazon Music has 6 menu items

  Scenario: Amazon Music has 6 menu items
    Given Open Amazon page
    When Click on hamburger menu
    And Click on Amazon Music menu item
    Then 6 menu items are present