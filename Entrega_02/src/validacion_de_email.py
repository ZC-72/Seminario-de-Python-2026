def validacion_de_email():
    valido = False
    email = input("Ingrese un email: ")

    # Valida que haya solo un @
    if email.count('@') == 1:
        # Valida que no empieze ni termine con @ o punto.
        if not email.startswith('@') and not email.endswith('.'):
            if not email.startswith('.') and not email.endswith('@'):
                email = email.split('@')
                # Verifica que haya al menos un caracter antes del @
                # Y al menos un punto despues.
                if len(email[0]) >= 1 and email[1].count('.') >= 1:
                    dominio = email[1].split('.')
                    # Y al menos dos caracteres despues del punto.
                    if len(dominio[-1]) >= 2:
                        valido = True
    # Imprime el mensaje correspondiente al valor de la variable valido.
    if valido: 
        print('El email es válido.')
    else:
        print('El email no es válido.')