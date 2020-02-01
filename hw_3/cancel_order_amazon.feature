# Created by arina at 2/1/20

Feature: Test Scenarios for search for Cancelling an order on Amazon

  Scenario: User can search for Cancelling an order on Amazon
    Given Open Amazon help page
    When Input Cancel order into search field
    And Click search button
    Then 'Cancel Items or Orders' page is shown
