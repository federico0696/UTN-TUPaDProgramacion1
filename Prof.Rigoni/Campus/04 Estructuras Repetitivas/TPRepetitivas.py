"""
TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA
Práctico 4: Estructuras repetitivas
Objetivo: Implementar ciclos para resolver problemas que requieran repetición de acciones
"""

import random

def ejercicio_1():
    """
    1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
    (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
    """
    print("=== EJERCICIO 1 ===")
    print("Números del 0 al 100:")
    for i in range(101):  # range(101) va de 0 a 100
        print(i)

def ejercicio_2():
    """
    2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
    dígitos que contiene.
    """
    print("\n=== EJERCICIO 2 ===")
    numero = int(input("Ingrese un número entero: "))
    
    # Convertir a valor absoluto para manejar números negativos
    numero_abs = abs(numero)
    contador_digitos = 0
    
    # Caso especial para el número 0
    if numero_abs == 0:
        contador_digitos = 1
    else:
        while numero_abs > 0:
            numero_abs //= 10  # División entera por 10  (numero_abs = numero_abs // 10) (divide por 10, se queda con la parte entera y descarta el resto)
            contador_digitos += 1
    
    print(f"El número {numero} tiene {contador_digitos} dígito(s)")

def ejercicio_3():
    """
    3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
    dados por el usuario, excluyendo esos dos valores.
    """
    print("\n=== EJERCICIO 3 ===")
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    
    # Asegurar que valor1 sea menor que valor2
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1
    
    suma = 0
    for i in range(valor1 + 1, valor2):  # Excluye los extremos
        suma += i
    
    print(f"La suma de los números entre {valor1} y {valor2} (excluyendo extremos) es: {suma}")

def ejercicio_4():
    """
    4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
    secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.
    """
    print("\n=== EJERCICIO 4 ===")
    print("Ingrese números enteros (0 para terminar):")
    
    suma_total = 0
    numero = int(input("Ingrese un número: "))
    
    while numero != 0:
        suma_total += numero
        numero = int(input("Ingrese un número: "))
    
    print(f"La suma total acumulada es: {suma_total}")

def ejercicio_5():
    """
    5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9.
    Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
    """
    print("\n=== EJERCICIO 5 ===")
    numero_secreto = random.randint(0, 9)
    intentos = 0
    adivinado = False
    
    print("¡Adivina el número entre 0 y 9!")
    
    while not adivinado:
        intento = int(input("Ingrese su número: "))
        intentos += 1
        
        if intento == numero_secreto:
            adivinado = True
            print(f"¡Correcto! El número era {numero_secreto}")
            print(f"Lo adivinaste en {intentos} intento(s)")
        elif intento < numero_secreto:
            print("El número es mayor")
        else:
            print("El número es menor")

def ejercicio_6():
    """
    6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
    entre 0 y 100, en orden decreciente.
    """
    print("\n=== EJERCICIO 6 ===")
    print("Números pares del 100 al 0 (orden decreciente):")
    
    for i in range(100, -1, -2):  # De 100 a 0, de a 2 (solo pares)
        print(i)

def ejercicio_7():
    """
    7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
    número entero positivo indicado por el usuario.
    """
    print("\n=== EJERCICIO 7 ===")
    numero = int(input("Ingrese un número entero positivo: "))
    
    while numero <= 0:
        print("El número debe ser positivo")
        numero = int(input("Ingrese un número entero positivo: "))
    
    suma = 0
    for i in range(1, numero + 1):  # De 1 hasta el número (incluido)
        suma += i
    
    print(f"La suma de los números de 1 a {numero} es: {suma}")

def ejercicio_8():
    """
    8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
    programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
    negativos y cuántos son positivos.
    """
    print("\n=== EJERCICIO 8 ===")
    
    # Para pruebas, usar una cantidad menor
    cantidad = 5  # Cambiar a 100 para la versión final
    print(f"Ingrese {cantidad} números enteros:")
    
    pares = 0
    impares = 0
    negativos = 0
    positivos = 0
    ceros = 0
    
    for i in range(cantidad):
        numero = int(input(f"Número {i+1}: "))
        
        # Contar pares e impares
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        # Contar positivos, negativos y ceros
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            ceros += 1
    
    print("\n--- RESULTADOS ---")
    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Números positivos: {positivos}")
    print(f"Números negativos: {negativos}")
    print(f"Ceros: {ceros}")

def ejercicio_9():
    """
    9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
    media de esos valores.
    """
    print("\n=== EJERCICIO 9 ===")
    
    # Para pruebas, usar una cantidad menor
    cantidad = 5  # Cambiar a 100 para la versión final
    print(f"Ingrese {cantidad} números enteros:")
    
    suma_total = 0
    
    for i in range(cantidad):
        numero = int(input(f"Número {i+1}: "))
        suma_total += numero
    
    media = suma_total / cantidad
    print(f"\nLa media de los {cantidad} números es: {media:.2f}")

def ejercicio_10():
    """
    10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
    usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
    """
    print("\n=== EJERCICIO 10 ===")
    numero = int(input("Ingrese un número entero: "))
    
    numero_original = numero
    numero_abs = abs(numero)  # Trabajar con valor absoluto
    numero_invertido = 0
    
    while numero_abs > 0:
        digito = numero_abs % 10  # Obtener el último dígito
        numero_invertido = numero_invertido * 10 + digito  # Agregarlo al resultado
        numero_abs //= 10  # Eliminar el último dígito
    
    # Si el número original era negativo, hacer negativo el resultado
    if numero_original < 0:
        numero_invertido = -numero_invertido
    
    print(f"El número {numero_original} invertido es: {numero_invertido}")

def menu_principal():
    """
    Menú principal para ejecutar los ejercicios
    """
    while True:
        print("\n" + "="*50)
        print("TRABAJO PRÁCTICO 4 - ESTRUCTURAS REPETITIVAS")
        print("="*50)
        print("1. Números del 0 al 100")
        print("2. Contar dígitos de un número")
        print("3. Suma entre dos valores (excluyendo extremos)")
        print("4. Suma acumulativa hasta 0")
        print("5. Juego de adivinanza")
        print("6. Números pares del 100 al 0")
        print("7. Suma de 1 hasta un número")
        print("8. Análisis de 100 números")
        print("9. Media de 100 números")
        print("10. Invertir dígitos de un número")
        print("11. Ejecutar todos los ejercicios")
        print("0. Salir")
        print("-"*50)
        
        opcion = input("Seleccione una opción (0-11): ")
        
        if opcion == "1":
            ejercicio_1()
        elif opcion == "2":
            ejercicio_2()
        elif opcion == "3":
            ejercicio_3()
        elif opcion == "4":
            ejercicio_4()
        elif opcion == "5":
            ejercicio_5()
        elif opcion == "6":
            ejercicio_6()
        elif opcion == "7":
            ejercicio_7()
        elif opcion == "8":
            ejercicio_8()
        elif opcion == "9":
            ejercicio_9()
        elif opcion == "10":
            ejercicio_10()
        elif opcion == "11":
            # Ejecutar todos los ejercicios (excepto los interactivos)
            ejercicio_1()
            print("\n" + "="*30)
            print("Ejercicios interactivos disponibles desde el menú:")
            print("- Ejercicio 2: Contar dígitos")
            print("- Ejercicio 3: Suma entre valores")
            print("- Ejercicio 4: Suma acumulativa")
            print("- Ejercicio 5: Juego de adivinanza")
            print("- Ejercicio 7: Suma hasta un número")
            print("- Ejercicio 8: Análisis de números")
            print("- Ejercicio 9: Media de números")
            print("- Ejercicio 10: Invertir dígitos")
            ejercicio_6()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        
        input("\nPresione Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    menu_principal()