*** Settings ***
Library  Dialogs

*** Test Cases ***
Test Manual Step
    Execute Manual Step   Hey, this is a manual step
    Execute Manual Step   Hey, this is a manual step with default error    default_error=myerr

Test Selection From User
    ${username}=     Get Selection From User     Select user name    user1   user2   admin

Test Value From User
    ${value}=        Get Value From User     Provide a name      default value
    ${secret}=       Get Value From User     Provide a password  hidden=yes

Test pause Execution
    Pause Execution
    Pause Execution  message=Execution stopped. Hit [Return] to continue.
