*** Settings ***
Library    RequestsLibrary

*** Keywords ***
Main url session
    Create Session    alias=main    url=https://reqres.in/