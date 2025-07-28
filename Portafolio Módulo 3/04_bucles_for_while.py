# Funciones
def mostrar_menu():
    print("\n--- Menú de opciones ---")
    print("1. Tabla de multiplicar")
    print("2. Calculadora de factorial")
    print("3. Salir")

def tabla_multiplicar():
    try:
        num = int(input("Ingresa un número para la tabla de multiplicar: "))
        print(f"\nTabla del {num}:")
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entero.")

def calcular_factorial():
    try:
        n = int(input("Ingresa un número para calcular su factorial: "))
        if n < 0:
            print("El factorial no está definido para números negativos.")
            return
        factorial = 1
        contador = 1
        while contador <= n:
            factorial *= contador
            contador += 1
        print(f"El factorial de {n} es {factorial}")
    except ValueError:
        print("Entrada inválida. Debes ingresar un número entero.")

# Bucle principal del programa
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        tabla_multiplicar()
    elif opcion == "2":
        calcular_factorial()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta nuevamente.")
