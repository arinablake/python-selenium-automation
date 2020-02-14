# Created by arina at 2/13/20
Feature: Verify that user can choose sheets color
  # Enter feature description here

  Scenario: User can choose sheets color

    Given Open Amazon sheets page
    When Get all sheets colors
    When Check every color has matching description
    When User chooses Beige color
    When Add an item to shopping cart
