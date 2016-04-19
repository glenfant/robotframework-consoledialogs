*** Settings ***
Library  ConsoleDialogs

*** Test Cases ***
Test Pause
    Pause Execution   Message de pause très long texte avec des caractères accentués qui peuvent être très longs.
    Pause Execution
    Pause Execution   Message de pause
    Pause Execution
    Pause Execution   Message de pause
    Pause Execution
    Pause Execution   Message de pause
    Pause Execution
