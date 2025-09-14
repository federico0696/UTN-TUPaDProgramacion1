"""
TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN A DISTANCIA
Práctico 5: Listas
Objetivo: Desarrollar la comprensión y la capacidad de manipular listas en Python
mediante la aplicación de conceptos fundamentales como la indexación, la
modificación de elementos, el uso de métodos integrados y el manejo de listas anidadas.
"""

def ejercicio_1():
    """
    1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
    """
    print("=== EJERCICIO 1 ===")
    print("Lista de múltiplos de 4 del 1 al 100:")
    
    # Crear lista con múltiplos de 4 usando range
    multiplos_4 = list(range(4, 101, 4))  # Desde 4 hasta 100, de 4 en 4
    
    print(f"Múltiplos de 4: {multiplos_4}")
    print(f"Cantidad de elementos: {len(multiplos_4)}")

def ejercicio_2():
    """
    2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
    penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
    indexing con números negativos!
    """
    print("\n=== EJERCICIO 2 ===")
    print("Lista de mis cosas favoritas:")
    
    # Lista con 5 elementos que me gustan
    mis_favoritos = ["pizza", "programación", "música", "viajar", "chocolate"]
    
    print(f"Lista completa: {mis_favoritos}")
    
    # Mostrar penúltimo elemento usando índice negativo
    penultimo = mis_favoritos[-2]  # -2 significa penúltimo
    print(f"El penúltimo elemento es: {penultimo}")
    
    # Alternativa usando índice positivo
    penultimo_alt = mis_favoritos[len(mis_favoritos) - 2]
    print(f"Verificación con índice positivo: {penultimo_alt}")

def ejercicio_3():
    """
    3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
    """
    print("\n=== EJERCICIO 3 ===")
    print("Creando lista vacía y agregando elementos:")
    
    # Crear lista vacía
    lista_vacia = []
    print(f"Lista inicial (vacía): {lista_vacia}")
    
    # Agregar tres palabras con append
    lista_vacia.append("python")
    lista_vacia.append("programación")
    lista_vacia.append("aprendizaje")
    
    print(f"Lista después de agregar elementos: {lista_vacia}")

def ejercicio_4():
    """
    4) Reemplazar el segundo y último valor de la lista "animales" con las palabras "loro" y "oso",
    respectivamente. Imprimir la lista resultante por pantalla.
    """
    print("\n=== EJERCICIO 4 ===")
    print("Modificando lista de animales:")
    
    # Lista original
    animales = ["perro", "gato", "conejo", "pez"]
    print(f"Lista original: {animales}")
    
    # Reemplazar segundo elemento (índice 1)
    animales[1] = "loro"
    
    # Reemplazar último elemento usando índice negativo
    animales[-1] = "oso"
    
    print(f"Lista modificada: {animales}")

def ejercicio_5():
    """
    5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
    numeros = [8, 15, 3, 22, 7]
    numeros.remove(max(numeros))
    print(numeros)
    """
    print("\n=== EJERCICIO 5 ===")
    print("Análisis del programa:")
    
    # Programa a analizar
    numeros = [8, 15, 3, 22, 7]
    print(f"Lista original: {numeros}")
    print(f"El número máximo es: {max(numeros)}")
    
    numeros.remove(max(numeros))
    print(f"Lista después de remove(max()): {numeros}")
    
    print("\n--- EXPLICACIÓN ---")
    print("¿Qué hace este programa?")
    print("1. Crea una lista con números: [8, 15, 3, 22, 7]")
    print("2. max(numeros) encuentra el valor máximo de la lista (22)")
    print("3. remove(22) elimina la PRIMERA ocurrencia del número 22")
    print("4. El resultado es la lista sin el elemento máximo")
    print("5. Si hubiera números repetidos, solo eliminaría el primero")

def ejercicio_6():
    """
    6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
    pantalla los dos primeros.
    """
    print("\n=== EJERCICIO 6 ===")
    print("Lista con saltos de 5 en 5:")
    
    # Crear lista del 10 al 30 con saltos de 5
    numeros_saltos = list(range(10, 31, 5))  # 10, 15, 20, 25, 30
    
    print(f"Lista completa: {numeros_saltos}")
    print(f"Los dos primeros elementos: {numeros_saltos[:2]}")
    print(f"Primer elemento: {numeros_saltos[0]}")
    print(f"Segundo elemento: {numeros_saltos[1]}")

def ejercicio_7():
    """
    7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista "autos" por dos nuevos valores
    cualesquiera.
    """
    print("\n=== EJERCICIO 7 ===")
    print("Modificando valores centrales de la lista autos:")
    
    # Lista original
    autos = ["sedan", "polo", "suran", "gol"]
    print(f"Lista original: {autos}")
    
    # Reemplazar índices 1 y 2 (valores centrales)
    autos[1] = "fiesta"
    autos[2] = "corolla"
    
    print(f"Lista modificada: {autos}")

def ejercicio_8():
    """
    8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
    directamente. Imprimir la lista resultante por pantalla.
    """
    print("\n=== EJERCICIO 8 ===")
    print("Creando lista de dobles:")
    
    # Crear lista vacía
    dobles = []
    print(f"Lista inicial: {dobles}")
    
    # Agregar el doble de 5, 10 y 15
    dobles.append(5 * 2)   # Doble de 5 = 10
    dobles.append(10 * 2)  # Doble de 10 = 20
    dobles.append(15 * 2)  # Doble de 15 = 30
    
    print(f"Lista de dobles: {dobles}")

def ejercicio_9():
    """
    9) Dada la lista "compras", cuyos elementos representan los productos comprados por
    diferentes clientes:
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    a) Agregar "jugo" a la lista del tercer cliente usando append.
    b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
    c) Eliminar "pan" de la lista del primer cliente.
    d) Imprimir la lista resultante por pantalla
    """
    print("\n=== EJERCICIO 9 ===")
    print("Manipulando lista anidada de compras:")
    
    # Lista original
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
    print(f"Lista original: {compras}")
    
    print("\nOperaciones:")
    
    # a) Agregar "jugo" a la lista del tercer cliente (índice 2)
    compras[2].append("jugo")
    print(f"a) Después de agregar 'jugo' al tercer cliente: {compras}")
    
    # b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente (índice 1)
    indice_fideos = compras[1].index("fideos")  # Encontrar índice de "fideos"
    compras[1][indice_fideos] = "tallarines"
    print(f"b) Después de cambiar 'fideos' por 'tallarines': {compras}")
    
    # c) Eliminar "pan" de la lista del primer cliente (índice 0)
    compras[0].remove("pan")
    print(f"c) Después de eliminar 'pan' del primer cliente: {compras}")
    
    print(f"\nLista final: {compras}")

def ejercicio_10():
    """
    10) Elaborar una lista anidada llamada "lista_anidada" que contenga los siguientes elementos:
    • Posición lista_anidada[0]: 15
    • Posición lista_anidada[1]: True
    • Posición lista_anidada[2][0]: 25.5
    • Posición lista_anidada[2][1]: 57.9
    • Posición lista_anidada[2][2]: 30.6
    • Posición lista_anidada[3]: False
    """
    print("\n=== EJERCICIO 10 ===")
    print("Creando lista anidada con estructura específica:")
    
    # Crear la lista anidada según las especificaciones
    lista_anidada = [
        15,                    # Posición [0]
        True,                  # Posición [1]
        [25.5, 57.9, 30.6],   # Posición [2] - sublista con 3 elementos
        False                  # Posición [3]
    ]
    
    print(f"Lista anidada creada: {lista_anidada}")
    
    print("\nVerificación de posiciones:")
    print(f"lista_anidada[0] = {lista_anidada[0]}")
    print(f"lista_anidada[1] = {lista_anidada[1]}")
    print(f"lista_anidada[2][0] = {lista_anidada[2][0]}")
    print(f"lista_anidada[2][1] = {lista_anidada[2][1]}")
    print(f"lista_anidada[2][2] = {lista_anidada[2][2]}")
    print(f"lista_anidada[3] = {lista_anidada[3]}")

def ejercicio_adicional_indexing():
    """
    Ejercicio adicional: Demostración de indexing positivo y negativo
    """
    print("\n=== EJERCICIO ADICIONAL: INDEXING ===")
    print("Demostración de índices positivos y negativos:")
    
    ejemplo = ["A", "B", "C", "D", "E"]
    print(f"Lista ejemplo: {ejemplo}")
    
    print("\nÍndices positivos:")
    for i in range(len(ejemplo)):
        print(f"  índice {i}: {ejemplo[i]}")
    
    print("\nÍndices negativos:")
    for i in range(-len(ejemplo), 0):
        print(f"  índice {i}: {ejemplo[i]}")
    
    print("\nSlicing ejemplos:")
    print(f"  ejemplo[1:4]: {ejemplo[1:4]}")      # Del índice 1 al 3
    print(f"  ejemplo[:3]: {ejemplo[:3]}")        # Primeros 3 elementos
    print(f"  ejemplo[2:]: {ejemplo[2:]}")        # Desde el índice 2 hasta el final
    print(f"  ejemplo[-2:]: {ejemplo[-2:]}")      # Últimos 2 elementos
    print(f"  ejemplo[::2]: {ejemplo[::2]}")      # Cada 2 elementos

def menu_principal():
    """
    Menú principal para ejecutar los ejercicios
    """
    while True:
        print("\n" + "="*60)
        print("TRABAJO PRÁCTICO 5 - LISTAS")
        print("="*60)
        print("1.  Múltiplos de 4 del 1 al 100")
        print("2.  Lista de favoritos y penúltimo elemento")
        print("3.  Lista vacía y append")
        print("4.  Modificar lista de animales")
        print("5.  Análisis de programa (remove + max)")
        print("6.  Lista con saltos de 5")
        print("7.  Modificar valores centrales de autos")
        print("8.  Lista de dobles")
        print("9.  Manipular lista anidada de compras")
        print("10. Crear lista anidada específica")
        print("11. Demostración de indexing (adicional)")
        print("0.  Salir")
        print("-"*60)
        
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
            ejercicio_adicional_indexing()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
        
        input("\nPresione Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    print("Trabajo Práctico 5 - Listas")
    print("Conceptos: indexación, slicing, métodos de listas, listas anidadas")
    menu_principal()