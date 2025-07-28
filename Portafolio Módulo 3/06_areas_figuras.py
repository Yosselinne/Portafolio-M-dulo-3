import math

# Funciones para calcular el área
def area_cuadro(lado):
    return lado * lado

def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    return math.pi * radio ** 2

def area_triangulo(base, altura):
    return (base * altura) / 2

def mostrar_menu():
    print("\n--- Calculadora de áreas ---")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Círculo")
    print("4. Triángulo")
    print("5. Salir")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("Elige una figura (1-5): ")

    if opcion == "1":
        lado = float(input("Ingresa el lado del cuadrado: "))
        resultado = area_cuadro(lado)
        print(f"Área del cuadrado: {resultado:.2f}")
    
    elif opcion == "2":
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        resultado = area_rectangulo(base, altura)
        print(f"Área del rectángulo: {resultado:.2f}")
    
    elif opcion == "3":
        radio = float(input("Ingresa el radio del círculo: "))
        resultado = area_circulo(radio)
        print(f"Área del círculo: {resultado:.2f}")
    
    elif opcion == "4":
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        resultado = area_triangulo(base, altura)
        print(f"Área del triángulo: {resultado:.2f}")
    
    elif opcion == "5":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intenta nuevamente.")
        continue

    repetir = input("¿Quieres calcular el área de otra figura? (s/n): ").strip().lower()
    if repetir != "s":
        print("Gracias por usar la calculadora de áreas.")
        break
