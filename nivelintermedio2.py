import random

# Solicita al usuario que ingrese las IPs separadas por comas
entrada = input("Ingresa las direcciones IP separadas por comas (ejemplo: 192.168.1.10,10.0.0.5,192.168.34.2): ")

# Convierte la entrada en una lista, quitando espacios extra
ips_servidores = [ip.strip() for ip in entrada.split(",")]

# Recorre cada IP en la lista
for ip in ips_servidores:
    # Simula la verificación de conectividad con un valor aleatorio
    respuesta_ping = random.choice([True, False])
    
    # Verifica el resultado y muestra el mensaje correspondiente
    if respuesta_ping:
        print(f"El servidor {ip} está respondiendo.")
    else:
        print(f"¡Alerta! El servidor {ip} no responde.")

