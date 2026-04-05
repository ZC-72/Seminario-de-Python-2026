def simulacion_de_competencia_de_cocina_y_ranking():

    rounds = [
        {
            'theme': 'Entrada',
            'scores': {
                'Valentina': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Mateo': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                'Camila': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Santiago': {'judge_1': 6, 'judge_2': 7, 'judge_3': 6},
                'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 8},
            }
        },
        {
            'theme': 'Plato principal',
            'scores': {
                'Valentina': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Mateo': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Camila': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
                'Santiago': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
                'Lucía': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
            }
        },
        {
            'theme': 'Postre',
            'scores': {
                'Valentina': {'judge_1': 7, 'judge_2': 8, 'judge_3': 7},
                'Mateo': {'judge_1': 9, 'judge_2': 9, 'judge_3': 8},
                'Camila': {'judge_1': 8, 'judge_2': 7, 'judge_3': 9},
                'Santiago': {'judge_1': 7, 'judge_2': 7, 'judge_3': 6},
                'Lucía': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
            }
        },
        {
            'theme': 'Cocina internacional',
            'scores': {
                'Valentina': {'judge_1': 8, 'judge_2': 9, 'judge_3': 9},
                'Mateo': {'judge_1': 7, 'judge_2': 6, 'judge_3': 7},
                'Camila': {'judge_1': 9, 'judge_2': 8, 'judge_3': 8},
                'Santiago': {'judge_1': 8, 'judge_2': 9, 'judge_3': 7},
                'Lucía': {'judge_1': 7, 'judge_2': 7, 'judge_3': 8},
            }
        },
        {
            'theme': 'Final libre',
            'scores': {
                'Valentina': {'judge_1': 9, 'judge_2': 8, 'judge_3': 9},
                'Mateo': {'judge_1': 8, 'judge_2': 9, 'judge_3': 8},
                'Camila': {'judge_1': 7, 'judge_2': 7, 'judge_3': 7},
                'Santiago': {'judge_1': 9, 'judge_2': 9, 'judge_3': 9},
                'Lucía': {'judge_1': 8, 'judge_2': 8, 'judge_3': 7},
            }
        }
    ]
    indice = 1
    tabla_de_posiciones = {}
    tabla_de_posiciones_sorted = ()

    # Toma los nombres de los participantes y crea una lista.
    participantes = rounds[0]['scores'].keys()

    # Con los nombres crea un diccionario.
    for participante in participantes:
        tabla_de_posiciones[participante] = {
            "Puntaje": 0,
            "Rondas ganadas": 0,
            "Mejor ronda" : 0
        }
    # Recorre las rondas.
    for indice, ronda in enumerate(rounds,1):
        print(f'\nRonda {indice} - {ronda['theme']}')

        # Acumula los puntajes de los jueces. 
        puntajes_acumulados = {
            nombre_de_cocinero: sum(puntajes.values())
            for nombre_de_cocinero, puntajes in ronda["scores"].items()
        }
        
        # Actualiza los datos de los participantes.
        for nombre_cocinero, puntaje in puntajes_acumulados.items():
            tabla_de_posiciones[nombre_cocinero]["Puntaje"] += puntaje
            tabla_de_posiciones[nombre_cocinero]["Mejor ronda"] = max(
                tabla_de_posiciones[nombre_cocinero]["Mejor ronda"],puntaje
            )
        
        # Determina el ganador de la ronda.
        ganador_de_ronda, puntos = max(puntajes_acumulados.items(), key=lambda item:item[1])
        tabla_de_posiciones[ganador_de_ronda]["Rondas ganadas"] += 1

        print(f"Ganador: {ganador_de_ronda} ({puntos})")

        # Ordena el diccionario como una lista de tuplas ordenada por puntaje.
        tabla_de_posiciones_sorted = sorted(tabla_de_posiciones.items(), 
                                            key=lambda item:item[1]["Puntaje"], 
                                            reverse=True)
        # Imprime el resultado de la ronda
        print(f"\nPuntaje despues de la ronda {indice}")
        for cocinero, puntaje_parcial in tabla_de_posiciones_sorted:
            print(f'{cocinero + ":":<12} {puntaje_parcial["Puntaje"]}')
    # Imprime la tabla final.
    print("Tabla de posiciones final:")
    print(f'{"Cocinero"+ " "*8}{"Puntaje" + " "*4}{"Rondas ganadas" + " "*3} {"Mejor ronda" + " "*3} {"Promedio"}')
    print("-"*68)
    for competidor, informacion in tabla_de_posiciones_sorted:
        promedio = informacion["Puntaje"]/ indice
        print(f'{competidor:<15} {informacion["Puntaje"]:<10} {informacion["Rondas ganadas"]:<17} {informacion["Mejor ronda"]:<14} {promedio:.1f}')
    print("-"*68)