Feature: Sign into e-mail account
  As a user I want to log in and check my e-mails

  Scenario Outline: Log in with valid data
    #Outline mowi behave ze bedzie to test sterowania danymi
    Given user is on Poczta Onet website
    When user fills valid username <username> and valid password <password> and submits it
    Then User can see email list

    Examples:
    #DELETED IF NOT USED BY 12 MONTHS
    |username|password|
    |janusz.marowski@onet.pl|XXXXX|  
    |j.rozewski@onet.pl     |XXXXX| 

  Scenario Outline: Log in with invalid data
    Given user is on Poczta Onet website
    When user fills invalid username <invalidusername> and invalid password <invalidpass> and submits it
    Then User can see alert about invalid date

    Examples:
    |invalidusername|invalidpass|
    |janusfgdgdfgdg@onet.pl|1XXXX|
    |natciaxdfgdgdfg1@wp.pl|1Xq!j2$Yx*8Mw7r$2|
