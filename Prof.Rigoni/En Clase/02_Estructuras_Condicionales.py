#lunes inicial | martes intermedio | miercoles avanzado | jueves practica hablada | viernes viajeros

fecha_completa = input("A continuación ingrese la fecha con el siguiente formato: (dia, DD/MM): ")

#Dividimos la respuesta del usuario en dos, tomando de referencia la ","
partes = fecha_completa.split(",")
nombre_dia = partes[0].strip() #asigno a la variable el valor de la 1era parte eliminando los espacios
nombre_dia = nombre_dia.lower()

#Tomamos la segunda parte y la dividimos en dos
fecha = partes[1].strip()
fecha_dia, fecha_mes = fecha.split("/")

#validamos formato
if len(fecha_dia) != 2:
    print("Error: el día y el mes deben tener dos caracteres."); exit()

if len(fecha_mes) != 2:
    print("Error, el día y el mes deben tener dos caracteres."); exit()

#convertimos a entero la fecha
try:
    fecha_dia = int(fecha_dia)
    fecha_mes = int(fecha_mes)
except ValueError:
    print("Error: el dia o el mes no son validos.")
    exit()

clases_dias = {
    "lunes" : "inicial",
    "martes" : "intermedio",
    "miercoles" : "avanzado",
    "jueves" : "practica",
    "viernes" : "viajeros"
} 

#informe de errores
if (fecha_dia > 31 or fecha_dia < 1):
    print("Error: la fecha del día no es válida."); exit()
elif (fecha_mes > 12 or fecha_mes < 1):
    print("Error: la fecha del mes no es válida."); exit()
elif nombre_dia not in clases_dias:
    print("Error: el nombre del día no es válido."); exit()

#determina el nivel segun el día ingresado
nivel = clases_dias[nombre_dia]
#procesa exámenes sólo para niveles con evaluación
if nivel in ["inicial","intermedio","avanzado"]:
    respuesta = input("Se tomaron examenes?: si / no: ").lower()
    if (respuesta == "si"):
        aprobados = int(input("Ingrese la cantidad de alumnos aprobados: "))
        desaprobados = int(input("Ingrese la cantidad de alumnos desaprobados: "))
        total = aprobados + desaprobados
        if (total > 0):
            porc_aprobados = (aprobados / total) * 100
            print(f"El porcentaje de aprobados es de: {porc_aprobados:.2f}%")
        else:
            print("No hay alumnos para calcular porcentaje.")

#porcentaje de asistencia en clase para practicas habladas
if (nivel == "practica"):
    porc_asistencia = float(input("Ingrese el porcentaje de asistencia: "))
    if porc_asistencia > 50:
        print("Asistió la mayoria.")
    else:
        print("No asistió la mayoria.")

#gestiona el inicio del ciclo para viajeros
if (nivel == "viajeros"):
    if ((fecha_dia == 1 and fecha_mes == 1) or (fecha_dia == 1 and fecha_mes == 7)):
        print("Comienzo de nuevo ciclo.")
        total_alumnos = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel = float(input("Ingrese el arancel en $ por cada alumno: "))
        ingreso_total = arancel * total_alumnos
        print(f"El ingreso total es de: ${ingreso_total}")
