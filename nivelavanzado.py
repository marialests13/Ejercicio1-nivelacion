import os
from collections import Counter

# Lista que almacenará los equipos como diccionarios
inventario = []

# Función para limpiar pantalla
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

# Función para agregar un equipo al inventario
def agregar_equipo():
    print("\n--- Agregar nuevo equipo ---")
    tipo = input("Tipo (ej: Laptop, PC, Impresora): ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    serial = input("Número de serie: ")
    ubicacion = input("Ubicación (ej: Oficina 1, Bodega): ")
    
    equipo = {
        "tipo": tipo,
        "marca": marca,
        "modelo": modelo,
        "serial": serial,
        "ubicacion": ubicacion
    }
    
    inventario.append(equipo)
    print("✅ Equipo agregado con éxito.\n")

# Función para buscar equipos según un criterio
def buscar_equipo():
    print("\n--- Buscar equipos ---")
    criterio = input("Buscar por (marca/tipo/ubicacion): ").lower()
    valor = input("Valor a buscar: ").lower()
    
    encontrados = [eq for eq in inventario if eq.get(criterio, "").lower() == valor]
    
    if encontrados:
        print(f"\nSe encontraron {len(encontrados)} equipo(s):")
        for eq in encontrados:
            print(f"- {eq['tipo']} | {eq['marca']} {eq['modelo']} | Serial: {eq['serial']} | Ubicación: {eq['ubicacion']}")
    else:
        print("❌ No se encontraron equipos con ese criterio.\n")

# Función para mostrar estadísticas
def ver_estadisticas():
    print("\n--- Estadísticas del inventario ---")
    tipos = Counter(eq['tipo'] for eq in inventario)
    ubicaciones = Counter(eq['ubicacion'] for eq in inventario)
    
    print("\nCantidad por tipo:")
    for tipo, cantidad in tipos.items():
        print(f"- {tipo}: {cantidad}")
    
    print("\nCantidad por ubicación:")
    for ubicacion, cantidad in ubicaciones.items():
        print(f"- {ubicacion}: {cantidad}")

# Función para generar informe detallado
def generar_informe():
    print("\n--- Informe del inventario ---")
    if not inventario:
        print("El inventario está vacío.")
    else:
        for i, eq in enumerate(inventario, start=1):
            print(f"{i}. Tipo: {eq['tipo']}, Marca: {eq['marca']}, Modelo: {eq['modelo']}, Serial: {eq['serial']}, Ubicación: {eq['ubicacion']}")
    print()

# Menú interactivo
def menu():
    while True:
        print("\n=== Sistema de Inventario ===")
        print("1. Agregar equipo")
        print("2. Buscar equipo")
        print("3. Ver estadísticas")
        print("4. Generar informe")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            agregar_equipo()
        elif opcion == "2":
            buscar_equipo()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            generar_informe()
        elif opcion == "5":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

# Ejecutar el menú
menu()
