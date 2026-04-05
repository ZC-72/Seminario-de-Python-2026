def estadisticas_de_un_texto():
    text = """Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!"""

    # Divide el texto en lineas.
    lineas = text.splitlines()
    # Divide las lineas en palabras.
    palabras = text.split()
    # Calcula el promedio de palabras.
    promedio = round(len(palabras)/len(lineas),2)
    # Imprime el total de linesa, palabras, promedio por linea.
    # Y las que estan por encima del promedio.
    print(f'Total de líneas: {len(lineas)}')
    print(f'Total de palabras: {len(palabras)}')
    print(f'Promedio de palabras por línea: {promedio}\n')
    print(f'Líneas por encima del promedio ({promedio} palabras):')
    # Imprime las lineas por encima del promedio y su cantidad de palabras.
    for elem in lineas:
        linea = elem.split()
        if len(linea) > promedio:
            print(f'- "{elem.strip()}" ({len(linea)} palabras) " -')