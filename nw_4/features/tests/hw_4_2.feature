Feature: Verify that user can count historic books
  # Enter feature description here

  Scenario: User can count historic books
    Given Open Amazon page
    When Search input fill history book
    And Click search button
    Then Amazon page will have 22 history book items

     When See last item
     Then Last item has Best Seller label
     When Click the item link
     When Add an item to shopping cart