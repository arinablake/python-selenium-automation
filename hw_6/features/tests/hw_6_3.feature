# Created by arina at 2/21/20
Feature: Verify that user can add a specific item to Cart and remove it

  Scenario: User can add a specific item to Cart and remove it
    Given Open webstaurant store
    When Search for stainless work table
    When Click search button
    When Check the search result ensuring every product item has the word Table its title
    When Add the last of found items to Cart
    Then Empty Cart
