while True:
    try:
        numero = float(input("Ingresa un número: "))

        if numero > 0:
            print("El número es positivo.")
        elif numero < 0:
            print("El número es negativo.")
        else:
            print("El número es cero.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
        continue

    opcion = input("¿Quieres ingresar otro número? (sí/no): ").strip().lower()
    if opcion != "sí":
        print("Programa finalizado.")
        break
