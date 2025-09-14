#---------- Ejercicio "FOR"
print("Ejercicio 1:")

abecedario = list("abcdefghijklmnñopqrstuvwxyz")
corrimiento = int(input("Ingrese el número de corrimiento: "))

#Pedir 5 mensajes al usuario
mensajes = []
for i in range(1, 6):
    mensaje = input(f"Ingrese el mensaje {i}: ")
    mensajes.append(mensaje)

mensajes_cifrados = []

#Encriptar cada mensaje
for mensaje in mensajes:
    cifrado = ""
    for letra in mensaje.lower(): 
        if letra in abecedario:
            i = abecedario.index(letra) #índice de la letra en "abecedario"
            cifrado += abecedario[(i + corrimiento) % len(abecedario)] #corre la letra original según lo indicado
        else:
            cifrado += letra #se mantiene igual si no esta en el abecedario
    mensajes_cifrados.append(cifrado)

for i in range(len(mensajes)):
    print(f"Mensaje original {i+1}: {mensajes[i]}")
    print(f"Mensaje cifrado {i+1}: {mensajes_cifrados[i]}\n")

#---------- Ejercicio "WHILE"
print("Ejercicio 2:")

import random
puntos_usuario = 0
puntos_maquina = 0
continuar = "s"

while continuar.lower() == "s":
    opciones = ["Piedra","Papel","Tijera"]
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

    usuario = int(input("Ingrese 1, 2 o 3: "))
    while usuario not in [1,2,3]:
        print("Opcion invalida.")
        usuario = int(input("Ingrese 1, 2 o 3: "))
    maquina = random.randint(1,3)
    print(f"El usuario eligio: {opciones[usuario-1]}.")
    print(f"La computadora eligio: {opciones[maquina-1]}.")

    if maquina == usuario:
        print("Empate.")
    elif (maquina == 1 and usuario == 2) or \
        (maquina ==2 and usuario == 3) or \
        (maquina == 3 and usuario ==1):
        print("Gana el usuario.")
        puntos_usuario += 1
    else:
        print("Gana la computadora.")
        puntos_maquina += 1
    continuar = input("¿Querés jugar otra vez? (s/n): ").lower()

if puntos_maquina > puntos_usuario:
    print(f"Historial: {puntos_maquina} / {puntos_usuario}. Computadora gana!")
elif puntos_maquina < puntos_usuario:
    print(f"Historial: {puntos_maquina} / {puntos_usuario}. Usuario gana!")
else:
    print(f"Historial: {puntos_maquina} / {puntos_usuario}. Termina en empate!")