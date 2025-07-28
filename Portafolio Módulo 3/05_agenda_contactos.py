# Diccionario
agenda = {}

# Funciones
def agregar_contacto():
    while True:
        nombre = input("Ingresa el nombre del contacto: ").strip()
        telefono = input("Ingresa el teléfono del contacto: ").strip()
        agenda[nombre] = telefono
        print(f"Contacto {nombre} agregado.\n")
        
        seguir = input("¿Quieres agregar otro contacto? (sí/no): ").strip().lower()
        if seguir != "sí":
            break

def mostrar_agenda():
    if not agenda:
        print("La agenda está vacía.\n")
        return
    print("\nAgenda:")
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")
    print()

def mostrar_menu():
    print("----- Menú Agenda -----")
    print("1. Agregar contacto")
    print("2. Mostrar agenda")
    print("3. Salir")
    print()

# Programa
while True:
    mostrar_menu()
    opcion = input("Elige una opción: ").strip()
    
    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        mostrar_agenda()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida, intenta nuevamente.\n")

