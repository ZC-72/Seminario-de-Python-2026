def analisis_de_hashtag():
    posts = [
        "Arrancando el lunes con energía #Motivación #NuevaSemana",
        "Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi", 
        "No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
        "Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
        "Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
        "Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
        "Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
        "Finde de lluvia, maratón de series #SerieAdicta #Relax",
        "Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
    ]
    Hashtags = {}
    # Busca en el texto las palabras que empiezan con hashtag.
    # Y las guarda en el diccionario Hasthtags.
    for post in posts:
        linea = post.split()
        for palabra in linea:
            if palabra.startswith("#"):
                Hashtags[palabra] = Hashtags.get(palabra, 0) + 1
    # Ordena la lista por el número de apariciones.
    sorted_Hashtag = sorted(Hashtags.items(), key=lambda item: item[1], reverse=True)
    # Imprime en pantalla las claves y los valores.
    print('Hashtags trending (más de una aparición):')
    for key,value in sorted_Hashtag:
        if value > 1:
            print(f'    {key}: {value}')
    print(f'Total de hashtags únicos: {len(sorted_Hashtag)}')