from utiles_es import pedir_entero, pedir_float,pedir_texto, pedir_opcion, validar_cuit

#------- Ejercicio N'01 "Sistema de Becas Estudiantiles" -------
print("Ejercicio 1: 'Sistema de Becas Estudiantiles' ")

nombre_completo = pedir_texto("Ingrese el nombre completo: ")
edad = pedir_entero("Ingres su edad: ", minimo= 15, maximo= 120)
promedio_general = pedir_float("Ingrese su promedio general: ", minimo= 0, maximo= 10)
ingresos_flia_mensuales = pedir_entero("Ingresos familiares mensuales: ")

if promedio_general < 6 or ingresos_flia_mensuales > 600000:
    resultado = "Rechazado"
elif ingresos_flia_mensuales < 300000:
        resultado = "Beca completa"
elif ingresos_flia_mensuales >= 300000 and ingresos_flia_mensuales <= 600000:
        resultado = "Media beca"
else:
    print("Error:datos ingresados invalidos")

print(f"{nombre_completo}, {edad} anios")
print(f"Promedio: {promedio_general}")
print(f"Ingresos: {ingresos_flia_mensuales}")
print(f"Resultado: {resultado}")

#------- Ejercicio N'02 "Gestion de Turnos Hospitalarios" -------
print("Ejercicio 2: 'Gestion de Turnos Hospitalarios' ")

nombre_completo = pedir_texto("Ingrese su nombre completo: ")
dni = pedir_entero("Ingrese su DNI: ",minimo= 1000000, maximo=99999999)
edad = pedir_entero("Ingrese su edad: ",minimo=0, maximo=120)
obra_social = pedir_opcion("Obra social: ",["si","no"])
prioridad_medica = pedir_opcion("Prioridad médica: (1 = emergencia, 2 = urgente, 3 = control.): ", [ "1","2","3"])

if prioridad_medica == "1" : 
    turno = "Guardia"
    print(f"Paciente: {nombre_completo}")
    print(f"Edad: {edad}")
    print(f"Prioridad: {prioridad_medica}")
    print(f"Turno asignado: {turno}")
    exit()
elif prioridad_medica == "2":
    if obra_social == "si" :
        turno = "En menos de 24hs"
    else:
        turno = "En 48hs"
elif prioridad_medica == "3" :
    if edad > 65:
        turno = "Preferencial en 72hs"
    else:
        turno = "En 7 dias"
else:
    print("Datos ingresados invalidos")

print(f"Paciente: {nombre_completo}")
print(f"Edad: {edad}")
print(f"Prioridad: {prioridad_medica}")
print(f"Turno asignado: {turno}")

#------- Ejercicio N'03 "Evaluacion de Credito Bancario" -------
print("Ejercicio 3: 'Evaluacion de Credito Bancario' ")

nombre_completo = pedir_texto("Ingrese su nombre completo: ")
cuit = validar_cuit("Ingrese su CUIT: ")
ingreso_mensuales = pedir_entero("Ingresos mensuales: ")
antiguedad_laboral = pedir_entero("Ingrese la antiguedad laboral (en anios): ")
historial_crediticio = pedir_opcion("Ingrese el historial crediticio: ",["bueno","regular","malo"])

if historial_crediticio == "malo" and ingreso_mensuales < 200000 :
    print("Usted fue rechazado.")
    exit()
elif ingreso_mensuales >= 200000 and antiguedad_laboral < 2:
    monto_aprobado = "$500,000"
elif ingreso_mensuales >= 200000 and antiguedad_laboral >= 2:
    if historial_crediticio == "regular":
        monto_aprobado = "$1,000,000"
    elif historial_crediticio == "bueno":
        monto_aprobado = "$3,000,000"
else:
    print("Datos invalidos")

print(f"Cliente: {nombre_completo}")
print(f"CUIT: {cuit}")
print(f"Ingresos: ${ingreso_mensuales}")
print(f"Antiguedad: {antiguedad_laboral} anios")
print(f"Historial: {historial_crediticio}")
print(f"Monto aprobado: {monto_aprobado}")

#------- Ejercicio N'04 "Clasificacion de Impuestos" -------
print("Ejercicio 4: 'Clasificacion de Impuestos' ")

nombre_completo = pedir_texto("Ingrese su nombre completo: ")
edad = pedir_entero("Ingrese su edad: ")
ingresos_anuales = pedir_entero("Ingresos anuales: ")

if ingresos_anuales < 500000 :
    impuestos = 0
elif ingresos_anuales >= 500000 and ingresos_anuales < 2000000 :
    impuestos = ingresos_anuales * 0.10
elif ingresos_anuales >= 2000000 and ingresos_anuales < 5000000 :
    impuestos = ingresos_anuales * 0.20
else:
    impuestos = ingresos_anuales * 0.35 
#Descuento por edad
if edad > 65 :
    impuestos /= 2

print(f"Nombre: {nombre_completo}")
print(f"Ingresos: ${ingresos_anuales}")
print(f"Edad: {edad}")
print(f"Impuesto final: ${impuestos}")

#------- Ejericio N'05 "Sistema de Calificaciones con Promocion" -------
print("Ejercicio 5: 'Sistema de Clasificacion con Promocion")

nombre_completo = pedir_texto("Ingrese su nombre completo: ")
legajo = pedir_entero("Ingrese el legajo: ")
nota1 = pedir_entero("Ingrese la primer nota: ",minimo=0, maximo=10)
nota2 = pedir_entero("Ingrese la segunda nota: ",minimo=0, maximo=10)
nota3 = pedir_entero("Ingrese la tercer nota: ",minimo=0, maximo=10)
promedio = (nota1 + nota2 + nota3) / 3

if nota1 < 4 or nota2 < 4 or nota3 <4:
    estado_academico = "Desaprobado"
elif promedio < 6 :
    estado_academico = "Desaprobado"
elif promedio >= 6 and promedio <= 7 :
    estado_academico = "Aprobado con final"
else :
    estado_academico = "Promocionado"
print(f"Alumno: {nombre_completo}")
print(f"Legajo: {legajo}")
print(f"Promedio: {promedio:.2f}")
print(f"Estado academico final: {estado_academico}")

#------- Ejercicio N'06 "Simulador de Cajero Automático" -------
print("Ejercicio 6: 'Simulador de Cajero Automatico' ")

nombre_usuario = pedir_texto("Ingrese su nombre de usuario: ")
pin = pedir_entero("Ingrese su pin: ")
saldo_inicial = 50000
print(f"Saldo inicial = ${saldo_inicial}")
max_intentos = 3 #intentos permitidos (PIN)

respuesta = pedir_opcion("Usted desea hacer un retiro? si / no : ",["si","no"]).lower()

if respuesta == "no":
    print("Vuelva pronto.")
    exit()

elif respuesta == "si":
    #Validar Pin
    for intento in range(1, max_intentos + 1):
        pin_ingresado = pedir_entero("Ingrese su PIN: ")
        if pin_ingresado == pin:
            print("PIN correcto. Bienvenido !")
            break
        else:
            print(f"PIN incorrecto. Intentos restantes: {max_intentos - intento}.")
    else:
        print("Demasiados intentos fallidos. Tarjeta bloqueada.")
        exit()

    monto_retirar = pedir_entero("Ingrese el monto que desea retirar: ")
    if monto_retirar % 1000 != 0 or monto_retirar > saldo_inicial:
        print("Monto no válido.")
        exit()
    else:
        if monto_retirar > 20000:
            comision = monto_retirar * 0.02
            print("Retiro realizado con exito.\nDebido a que el saldo retirado superó los $20.000 se cobró un 2% de comisión.")
            saldo_actual = saldo_inicial - monto_retirar - comision
            print(f"Saldo actual: ${saldo_actual}")
        else:
            print("Retiro con exito")
            saldo_actual = saldo_inicial - monto_retirar
            print(f"Saldo actual: ${saldo_actual}")
else:
    exit()

#------- Ejercicio N´07 "Cateoria de Conductores" -------
print("Ejercicio 7: 'Categoria de Conductores' ")

nombre_completo = pedir_texto("Ingrese su nombre completo: ")
edad = pedir_entero("Ingrese su edad: ")
anios_exp = pedir_entero("Años de experiencia conduciendo: ")

if edad < 18 :
    print("Usted no puede conducir")
    exit()
elif edad >= 30 and anios_exp > 10:
    categoria = "conductor profesional. "
elif edad >= 21 and 1 <= anios_exp <= 5:
    categoria = "conductor intermedio"
elif edad >= 18 and anios_exp < 1:
    categoria = "conductor principiante."
else:
    categoria = "conductor estándar."

print(f"Usted es un {categoria}")

#------- Ejercicio N´08 "Simulador de Carrito de Compras" -------
print("Ejercicio 8: 'Simulador de Carrito de Compras' ")

nombre = pedir_texto("Ingrese su nombre: ")
cant_productos = pedir_entero("Cantidad de productos: ",minimo=0)
monto_total = pedir_float("Ingrese el monto total de la compra: ",minimo=0)
pago = pedir_opcion("Medio de pago: ",["efectivo","debito","credito","mercado pago"])

descuento = 0
desc_porcentaje = 0
recargo = 0
rec_porcentaje = 0

if pago == "efectivo" :
    descuento = monto_total * 0.15
    desc_porcentaje = 15
elif pago == "debito":
    descuento = monto_total * 0.10
    desc_porcentaje = 10
elif pago == "credito":
    recargo = monto_total * 0.05
    descuento = 0
    rec_porcentaje = 5
elif pago == "mercado pago" :
    if monto_total > 10000:
        descuento = monto_total * 0.20
        desc_porcentaje = 20

total_final = monto_total - descuento + recargo
desc_extra = 0

if cant_productos > 10:
    desc_extra = total_final * 0.05
    total_final -= desc_extra

print(f"Importe total: ${monto_total:.2f}")
print(f"Descuento aplicado: ${descuento:.2f} ({desc_porcentaje}%)")
print(f"Recargo aplicado: ${recargo:.2f} ({rec_porcentaje}%)")
if desc_extra > 0:
    print(f"Descuento adicional por cantidad de productos: ${desc_extra:.2f} (5%)" )

print(f"Importe final: ${total_final:.2f}")