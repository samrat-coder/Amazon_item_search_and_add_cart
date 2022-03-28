Feature: laptop_add_cart
    Scenario: laptop_add_cart
        Given User create driver
        And   User open url
        When  user search item 'laptop'
        And   user click brand name
        And   user select first item
        And   switch to window
        And   user cart item
       # And   close popup window
        Then  user close driver



