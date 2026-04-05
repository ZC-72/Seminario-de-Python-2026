def ejecutar_cifrado_cesar():
    
    def cifrado_cesar(texto,desplazamiento):
        texto_cifrado = ""
        for char in texto:
            # Determina si el char es alphanumerico y lo desplaza.
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                char_cifrado = chr((ord(char) - base + desplazamiento) % 26 + base)
                texto_cifrado += char_cifrado
            # Sino lo agrega tal cual.
            else:
                texto_cifrado += char
        return texto_cifrado
    texto_a_cifrar = input('Ingrese texto a cifrar: ')

    # Valida que se ingrese un entero.
    while True:
        clave = input('Ingrese la cantidad a desplazarse: ')
        if clave.isdigit():
            clave = int(clave)
            break
        else:
            print('Ingrese un número entero.')
    
    # Realiza las invocaciones e imprime el mensaje.
    resultado_de_cifrar = cifrado_cesar(texto_a_cifrar,clave)
    print(f'Mensaje cifrado: {resultado_de_cifrar}')
    resultado_de_descifrar = cifrado_cesar(resultado_de_cifrar, -clave)
    print(f'Mensaje descifrado: {resultado_de_descifrar}')