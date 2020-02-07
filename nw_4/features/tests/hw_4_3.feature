# Created by arina at 2/7/20
Feature: Verify if there are 8 boxes on amazon prime page
  # Enter feature description here

  Scenario: User can verify if there are 8 boxes on amazon prime page

    Given Open Amazon prime page
    When See box
    Then Amazon prime page will have 8 boxes
