# Programación 1 - Ejercicios de Variables en Python
# El resultado de cada ejercicio debe mostrarse por pantalla.
# Las variables deben quedar todas en el archivo entregado.

# 1. Crea una variable llamada "numero1" y asígnale un número entero de tu elección.
numero1 = 10
print("numero1 =", numero1)

# 2. No borres la variable número1 y crea una variable llamada "numero2" asignándole un número decimal.
numero2 = 5.5
print("numero2 =", numero2)

# 3. Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2".
suma = numero1 + numero2
print("suma =", suma)

# 4. Crear variables para resta, multiplicación y división.
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print("resta =", resta)
print("multiplicacion =", multiplicacion)
print("division =", division)

# 5. Crea una variable llamada "nombre" y asígnale tu nombre como valor.
nombre = "Federico"
print("nombre =", nombre)

# 6. Crea una variable llamada "precio" y asígnale un valor decimal.
precio = 135.0
print("precio =", precio)

# 7. Crea una variable llamada "descuento" y asígnale un valor decimal.
descuento = 0.55
print("descuento =", descuento)

# 8. Calcula el precio final aplicando el descuento al precio original.
precio_final = precio * (1 - descuento)
print("precio_final =", precio_final)

# 9. Crea una variable llamada "cadena" y asígnale un texto.
cadena = "No se me ocurre que poner"
print("cadena =", cadena)

# 10. Crea una variable llamada "longitud" con la longitud de la cadena.
longitud = len(cadena)
print("longitud =", longitud)

# 11. Crea otra vez la variable "precio" y conviértelo en entero.
precio = 70.25
precio_entero = int(precio)
print("precio (decimal) =", precio)
print("precio_entero =", precio_entero)

# 12. Crea dos variables "nombre" y "apellido", concaténalas en "nombre_completo".
nombre = "Federico"
apellido = "Lopez"
nombre_completo = nombre + " " + apellido
print("nombre_completo =", nombre_completo)

# 13. Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10.
edad = 28
edad += 5
edad -= 10
print("edad =", edad)

# 14. Crea una variable "altura" y realiza operaciones.
altura = 1.83
altura_multi = altura * 4
altura_div = altura / 3
print("altura =", altura)
print("altura x4 =", altura_multi)
print("altura /3 =", altura_div)

# 15. Crea una variable con tu nombre en mayúsculas y luego en minúsculas.
nombre_mayus = nombre.upper()
nombre_minus = nombre_mayus.lower()
print("nombre_mayus =", nombre_mayus)
print("nombre_minus =", nombre_minus)

# 16. Con el nombre en mayúsculas, aplica un método para que solo la primera letra sea mayúscula.
nombre_capitalizado = nombre_mayus.capitalize()
print("nombre_capitalizado =", nombre_capitalizado)