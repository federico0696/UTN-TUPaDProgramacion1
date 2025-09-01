"""
Práctico 3: Estructuras condicionales
Tecnicatura Universitaria en Programación - UTN
"""

import random
from statistics import mode, median, mean

def ejercicio_1():
    """Ejercicio 1: Verificar mayor de edad"""
    print("EJERCICIO 1 - MAYOR DE EDAD")
    
    edad = int(input("Ingrese su edad: "))
    
    if edad > 18:
        print("Es mayor de edad")

def ejercicio_2():
    """Ejercicio 2: Verificar aprobación por nota"""
    print("EJERCICIO 2 - APROBACIÓN POR NOTA")
    
    nota = float(input("Ingrese su nota: "))
    
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

def ejercicio_3():
    """Ejercicio 3: Verificar número par"""
    print("EJERCICIO 3 - NÚMEROS PARES")
    
    numero = int(input("Ingrese un número: "))
    
    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")

def ejercicio_4():
    """Ejercicio 4: Categorías por edad"""
    print("EJERCICIO 4 - CATEGORÍAS POR EDAD")
    
    edad = int(input("Ingrese su edad: "))
    
    if edad < 12:
        print("Niño/a: menor de 12 años")
    elif edad >= 12 and edad < 18:
        print("Adolescente: mayor o igual que 12 años y menor que 18 años")
    elif edad >= 18 and edad < 30:
        print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años")
    elif edad >= 30:
        print("Adulto/a: mayor o igual que 30 años")

def ejercicio_5():
    """Ejercicio 5: Validar longitud de contraseña"""
    print("EJERCICIO 5 - VALIDAR CONTRASEÑA")
    
    contraseña = input("Ingrese una contraseña: ")
    longitud = len(contraseña)
    
    if longitud >= 8 and longitud <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

def ejercicio_6():
    """Ejercicio 6: Análisis de sesgo estadístico"""
    print("EJERCICIO 6 - ANÁLISIS DE SESGO ESTADÍSTICO")
    
    # Generar números aleatorios
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
    
    print("Lista de números aleatorios generada (50 números entre 1 y 100)")
    print(f"Primeros 10 números: {numeros_aleatorios[:10]}")
    
    # Calcular estadísticas
    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)
    
    print(f"Moda: {moda}")
    print(f"Mediana: {mediana}")
    print(f"Media: {media:.2f}")
    
    # Determinar sesgo
    if media > mediana and mediana > moda:
        print("La distribución tiene sesgo positivo o a la derecha")
    elif media < mediana and mediana < moda:
        print("La distribución tiene sesgo negativo o a la izquierda")
    elif media == mediana and mediana == moda:
        print("La distribución no tiene sesgo")
    else:
        print("La distribución no sigue un patrón clásico de sesgo")

def ejercicio_7():
    """Ejercicio 7: Añadir exclamación si termina en vocal"""
    print("EJERCICIO 7 - EXCLAMACIÓN SI TERMINA EN VOCAL")
    
    texto = input("Ingrese una frase o palabra: ")
    vocales = "aeiouAEIOU"
    
    if len(texto) > 0 and texto[-1] in vocales:
        resultado = texto + "!"
        print(resultado)
    else:
        print(texto)

def ejercicio_8():
    """Ejercicio 8: Transformar nombre según opción"""
    print("EJERCICIO 8 - TRANSFORMAR NOMBRE")
    
    nombre = input("Ingrese su nombre: ")
    print("Opciones:")
    print("1. Nombre en mayúsculas")
    print("2. Nombre en minúsculas")
    print("3. Nombre con la primera letra mayúscula")
    
    opcion = int(input("Seleccione una opción (1, 2 o 3): "))
    
    if opcion == 1:
        resultado = nombre.upper()
        print(resultado)
    elif opcion == 2:
        resultado = nombre.lower()
        print(resultado)
    elif opcion == 3:
        resultado = nombre.title()
        print(resultado)
    else:
        print("Opción inválida")

def ejercicio_9():
    """Ejercicio 9: Clasificar terremoto según escala de Richter"""
    print("EJERCICIO 9 - ESCALA DE RICHTER")
    
    magnitud = float(input("Ingrese la magnitud del terremoto: "))
    
    if magnitud < 3:
        print("Muy leve (imperceptible)")
    elif magnitud >= 3 and magnitud < 4:
        print("Leve (ligeramente perceptible)")
    elif magnitud >= 4 and magnitud < 5:
        print("Moderado (sentido por personas, pero generalmente no causa daños)")
    elif magnitud >= 5 and magnitud < 6:
        print("Fuerte (puede causar daños en estructuras débiles)")
    elif magnitud >= 6 and magnitud < 7:
        print("Muy Fuerte (puede causar daños significativos)")
    elif magnitud >= 7:
        print("Extremo (puede causar graves daños a gran escala)")

def ejercicio_10():
    """Ejercicio 10: Determinar estación del año según hemisferio"""
    print("EJERCICIO 10 - ESTACIONES DEL AÑO")
    
    estacion = "!Error algo salio mal¡ intente de nuevo"
    hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
    mes = int(input("¿Qué mes del año es? (1-12): "))
    dia = int(input("¿Qué día es? (1-31): "))
    
    # Hemisferio Norte
    if hemisferio == "N":
        if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
            estacion = "Primavera"
        elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
            estacion = "Verano"
        elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
            estacion = "Otoño"
    
    # Hemisferio Sur
    elif hemisferio == "S":
        if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
            estacion = "Otoño"
        elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <= 20):
            estacion = "Primavera"
    
    print(f"Se encuentra en {estacion}")

def menu_principal():
    """Menú para ejecutar los ejercicios"""
    print("PRÁCTICO 3: ESTRUCTURAS CONDICIONALES")
    print("Tecnicatura Universitaria en Programación - UTN")
    
    while True:
        print("MENÚ DE EJERCICIOS:")
        print("1. Mayor de edad")
        print("2. Aprobación por nota")
        print("3. Números pares")
        print("4. Categorías por edad")
        print("5. Validar contraseña")
        print("6. Análisis estadístico")
        print("7. Exclamación si termina en vocal")
        print("8. Transformar nombre")
        print("9. Escala de Richter")
        print("10. Estaciones del año")
        print("0. Salir")
        
        opcion = input("¿Qué ejercicio desea ejecutar? (0 para salir): ")
        
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
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Seleccione un número del 0 al 10.")
        
        input("Presione ENTER para continuar...")

# Ejecutar el programa
menu_principal()