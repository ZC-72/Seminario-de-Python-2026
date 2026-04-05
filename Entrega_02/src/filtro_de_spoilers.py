def filtro_de_spoilers():
    review = """La película sigue a un grupo de astronautas que
viajan a Marte
en una misión de rescate. El capitán Torres lidera al equipo
a través
de tormentas solares y fallos en el sistema de navegación. Al
llegar
a Marte descubren que la base está abandonada y los
suministros
destruidos. Torres decide sacrificar la nave nodriza para
salvar
al equipo y logran volver a la Tierra en una cápsula de
emergencia.
El final revela que Torres sobrevivió gracias a un pasaje
secreto."""
    
    # Pide palabas por teclado, les hace lower y las didive en las comas.
    spoilers = input("Ingrese las palabras spoiler (seperadas por coma): ")
    spoilers = spoilers.lower().split(',')
    palabra = ""
    redacted = []

    # Reconstruye el texto, redactando las palabras ingresadas.
    for c in review:
        if c.isalpha():
            palabra += c
        else:
            for spoil in spoilers:
                if palabra.lower() == spoil.strip():
                    palabra = '*'* len(spoil)
                    break
            redacted.append(palabra)
            redacted.append(c)
            palabra = ""
    # Corrige el formato e imprime.
    redacted = ''.join(redacted)
    print(redacted)