def calculadora_costo_de_envio():
    peso_zona = [
        {"local":"$500","regional":"$1000","nacional":"$2000"},
        {"local":"$1000","regional":"$2500","nacional":"$4500"},
        {"local":"$2000","regional":"$5000","nacional":"$8000"},
    ]
    # Verifica que le peso se mayor a cero.
    peso = input("Ingrese el peso del paquete (kg): ")
    while float(peso) < 0:
         peso = input("Ingrese un peso mayor a 0:")
    # Verifica que la zona sea valida.
    destino = input("Ingrese la zona del destino (local/regional/nacional):")
    while destino != "local" and destino !="regional" and destino !="nacional":
         destino = input("Zona no válida. Las zonas disponibles son: local, regional, nacional.")
    # Asigna la posicio correspondiente en la lista.
    if float(peso) < 1:
        output = peso_zona[0][destino]
    elif float(peso)< 5:
        output = peso_zona[1][destino]
    else:
        output = peso_zona[2][destino]
    print(f"Costo de envío: {output}")
            