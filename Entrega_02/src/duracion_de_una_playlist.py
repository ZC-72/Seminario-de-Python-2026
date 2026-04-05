def duracion_de_una_playlist():
    playlist = [
        {"title": "Bohemian Rhapsody", "duration": "5:55"},
        {"title": "Hotel California", "duration": "6:30"},
        {"title": "Stairway to Heaven", "duration": "8:02"},
        {"title": "Imagine", "duration": "3:07"},
        {"title": "Smells Like Teen Spirit", "duration": "5:01"},
        {"title": "Billie Jean", "duration": "4:54"},
        {"title": "Hey Jude", "duration": "7:11"},
        {"title": "Like a Rolling Stone", "duration": "6:13"},
    ]
    minutos = 0
    segundos = 0
    maxAndMin = []
    dMaximo = -1
    dMinimo = 999

    # Recorre la lista sumando minutos y segundos.
    for cancion in playlist:
        duracion = cancion["duration"].split(':')
        minutos += int(duracion[0])
        if segundos > 60:
            segundos = (segundos - 60) + int(duracion[1])
            minutos += 1
        else: segundos += int(duracion[1])
        candidato = (int(duracion[0]) * 60) + int(duracion[1])
        # Determina cancion minima y maxima.
        if candidato > dMaximo:
            dMaximo = candidato
            maxAndMin.insert(0,cancion)
        elif candidato < dMinimo:
            dMinimo = candidato
            maxAndMin.insert(1,cancion)
    # Imprime los resultados.
    print(f"Duración total: {minutos}m {segundos}s")
    print(f'Canción más larga: {maxAndMin[0]["title"]} ({maxAndMin[0]["duration"]})')
    print(f'Canción más corta: {maxAndMin[1]["title"]} ({maxAndMin[1]["duration"]})')