print("Formulario de registro\n")
nombre = input("Nombre: ")
edad = int(input("Edad: "))
altura = float(input("Altura (en metros): "))
acepta = input("¿Acepta los términos? (Sí/No): ").lower() == "sí" or "si"

print("\nResumen:\n")
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"Altura: {altura} m")
print(f"Acepta términos: {'Sí acepta los términos' if acepta else 'No acepta los términos'}")
