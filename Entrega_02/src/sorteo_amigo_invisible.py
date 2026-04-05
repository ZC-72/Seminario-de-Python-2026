import random

def sorteo_amigo_invisible():

    # Valida que los participantes sean al menos 3.
    while True:
        participantes = input("Ingrese los participantes (separados por coma): ")
        participantes = [n.strip() for n in participantes.split(",") if n.strip()]
        participantes = list({n.lower().capitalize() for n in participantes})
        if len(participantes) > 2:
            break
        else: 
            print('Ingrese al menos tres nombres.')
    # Reordena la lisa aleatoriamente.
    random.shuffle(participantes)
    asignaciones = {}
    # Verifica que no se repitan los nombres y no se asignen a si mismos.
    for indice, participante in enumerate(participantes):
        asignaciones[participante] = participantes[(indice + 1) % len(participantes)]
    # Imprime los resultados.
    for key, value in asignaciones.items():
        print(f'{key} --> {value}')