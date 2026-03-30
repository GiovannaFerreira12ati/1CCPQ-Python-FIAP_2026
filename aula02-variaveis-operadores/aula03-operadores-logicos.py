#LOGICA E (and)

verifica_email=True

verifica_senha=False

verifica_login=verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no programa!")

    #LOGICA OU(or)
    logica_ou= False or True or False
    print(logica_ou)

    #OPERADOE DE NEGACAO (not)
    negacao=not False
    print(negacao)

    if not verifica_login:
        print("Loga certo aí...")