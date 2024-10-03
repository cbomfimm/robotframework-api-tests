*** Settings ***
Library    JSONLibrary
Library    RequestsLibrary
Library    ../utils/utils.py
Resource    ../resources/main.resource

*** Test Cases ***
Rota de listagem de usuários
    Main url session
    ${response}    GET On Session    alias=main    url=/api/users
    Log    ${response}

    Status Should Be    200    ${response}    O status da requisição não é 200
    