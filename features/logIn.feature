Feature: YouTube Login
  Scenario Outline: User login
    Given User is on Facebook website
    When User types personal informations: <email> and <password>
    And Clicks on LogIn button
    Then User should get: <massageLink> on site

    Examples: User Data
    |email                     |password |massageLink|
    |usermail@gmail.com        |wrongPass|Forgot Password?       |
    |nonExistingUser@gmail.com |rightPass|Sign up for an account.|
    |*                         |rightPass|Sign up for an account.|
    |usermail2@gmail.com       |*        |Forgot Password?       |
