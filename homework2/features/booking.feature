Feature: Booking a Movie

    Scenario: Viewing movie page
    Given the application is running
    When a user checks the movie page
    Then the page should successfully load

    Scenario: Creating a movie
    Given the application is running
    When a user submits a movie
    Then a movie should be created

    Scenario: Viewing seats
    Given the application is running
    When a user checks the seats page
    Then the page should successfully load

    Scenario: Creating a Booking
    Given the application is running
    When a user submits a booking
    Then a booking should be created

