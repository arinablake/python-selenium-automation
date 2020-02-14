# Created by arina at 2/13/20
Feature: Verify that user can count best sellers fantasy books
  # Enter feature description here

  Scenario: User can count best sellers fantasy books
    Given Open Amazon page
    When Search input fill fantasy book
    And Click search button
    Then Counting best sellers fantasy books

