Feature: Send new e-mail
  As a log user I want to send an e-mail to my friend

  Scenario: Send an e-mail
    Given user is log on Poczta Onet
    When logo is there
    And user click button Napisz wiadomosc
    And user puts address recipient
    And user puts title of e-mail
    And user puts text of message
    And user click Wyslij button
    Then User send e-mail to friend