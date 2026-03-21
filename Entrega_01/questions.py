import random

categorias = {
    "general": ["python","programa",],
    "definible": ["variable","funcion"],
    "primitivas":["cadena","entero",],
    "iterables":["bucle","lista",]
}
terminar = False
puntajeTotal = 0
print("¡Bienvenido al Ahorcado")
print()
print("Ingrese una categoria de palabras:")
print()
print("general, definible, primitivas o iterables.")
print()
categoria = input()
sample = random.sample(categorias[categoria],len(categorias[categoria]))
while len(sample) > 0 and not terminar:
    word = random.choice(sample)
    sample.remove(word)
    guessed = []
    attemps = 6
    while attemps > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        # Verificar si el jugador ya adivinó la palabra completa

        if "_" not in progress:
            print("¡Ganaste!")
            break

        print(f"Intentos restantes: {attemps}")
        print(f"Letras usadas: {', '.join(guessed)}")

        letter = input("Ingresá una letra: ")
        if len(letter) == 1 and letter.isalpha():
            letter = letter.lower()
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra esta en la palabra.")
            else:
                guessed.append(letter)
                attemps -= 1
                print("Esa letra no está en la palabra.")

            print()
        else:
            print("Entrada no válida")

    else:
        print(f"¡Perdiste! La palabra era: {word}")
    print(f"Tu puntaje fue: {attemps}")
    puntajeTotal += attemps
    if len(sample) > 0:
        continuar = input("¿Queres seguir jugando?")
        if continuar == "no":
            terminar = True
    else: 
        print("Ya fueron usadas todas las palabras de la categoria.")
print(f"Puntaje total: {puntajeTotal}")

