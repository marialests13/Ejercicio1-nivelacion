# 1. Defina una variable llamada espacio_libre_gb y asígnale un valor numérico que represente la cantidad de espacio libre en gigabytes.
print("Por favor, indique cuanto espacio libre tiene libre")
espacio_libre_gb = int(input())

# 2. Utiliza una estructura condicional (if/elif/else) para generar una alerta según el espacio libre.
# 3. Si es menor a 10GB
if espacio_libre_gb < 10:
    print("¡Alerta! El espacio libre en disco es crítico. Requiere limpieza urgente")
elif espacio_libre_gb in range(10,51):
    print("Advertencia: El espacio libre en disco es bajo. Considere realizar una revisión")
elif espacio_libre_gb > 50:
    print("El espacio libre en disco es adecuado.")