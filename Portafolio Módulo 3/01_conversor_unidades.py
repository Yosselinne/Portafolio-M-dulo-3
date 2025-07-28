# Funciones
def conversor_temperatura():
    print("\nConversión de temperatura:")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        celsius = float(input("Ingresa temperatura en °C: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit:.2f}°F\n")
    elif opcion == "2":
        fahrenheit = float(input("Ingresa temperatura en °F: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius:.2f}°C\n")
    else:
        print("Opción no válida.\n")

def conversor_monedas():
    print("\nConversión de monedas:")
    print("1. CLP a USD")
    print("2. USD a CLP")
    opcion = input("Elige una opción: ")
    
    tasa_dolar = 900  # Tasa fija

    if opcion == "1":
        pesos = float(input("Ingresa cantidad en CLP: $"))
        dolares = pesos / tasa_dolar
        print(f"${pesos} CLP = ${dolares:.2f} USD\n")
    elif opcion == "2":
        dolares = float(input("Ingresa cantidad en USD: $"))
        pesos = dolares * tasa_dolar
        print(f"${dolares} USD = ${pesos:.2f} CLP\n")
    else:
        print("Opción no válida.\n")

def conversor_longitudes():
    print("\nConversión de longitud:")
    print("1. Metros a pies")
    print("2. Pies a metros")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        metros = float(input("Ingresa longitud en metros: "))
        pies = metros * 3.281
        print(f"{metros} metros = {pies:.2f} pies\n")
    elif opcion == "2":
        pies = float(input("Ingresa longitud en pies: "))
        metros = pies / 3.281
        print(f"{pies} pies = {metros:.2f} metros\n")
    else:
        print("Opción no válida.\n")

def mostrar_menu():
    print("--- Elige un tipo de conversor ---")
    print("1. Conversor de temperatura")
    print("2. Conversor CLP y USD")
    print("3. Conversor metros y pies")
    print("4. Salir")
    print()

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Ingresa una opción: ")

    if opcion == "1":
        conversor_temperatura()
    elif opcion == "2":
        conversor_monedas()
    elif opcion == "3":
        conversor_longitudes()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intenta nuevamente.\n")
