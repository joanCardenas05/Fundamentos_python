# ------------------------------------ejercicio 1

print("=" *100)
nombre = input("¿Cual es tu nombre? ")
valor_producto = input("¿Cual es el valor del productos? ")
promedio_asignarura = input("¿Cual es el promedio de asignatura? ")

print(f"\n yo soy, {nombre}, el valor del productoes es : {valor_producto}, y su promedio es: {promedio_asignarura} ")
print("=" *100)
print("-" *100)

# ---------------------------------------ejercicio 2

print("=" *100)
variable_1_entera = int(input("ingrese un numero entero: "))
variable_2_entera = int(input("ingrese otro numero entero: "))
variable_float = float(input("ingrese un numero decimal: "))
variable_1_string = input("ingrese una cadena de texto: ")
variable_2_string = input("ingrese otra cadena de texto:  ")
print()

suma_numeros = variable_1_entera + variable_2_entera + variable_float

print(f"La suma de los tres valores ingresados es: {suma_numeros}")
print()

numero_mayor = max (variable_1_entera, variable_2_entera, variable_float)
print(f"El numero mayor de tus numero ingresados es: {numero_mayor}")
print()

division_enteros = variable_1_entera // variable_2_entera
division_float =  variable_float / division_enteros 
print(f"La division del valor decimal con el resultado de los enteros es: {division_float}")
print()

print(f"las cadenas laidas son: {variable_1_string} y {variable_2_string}")
print("=" *100)
print("-" *100)

# -------------------------------Ejercicio 3 

print("=" *100)
base = int(input("ingrese un valor de base: "))
exponente = int(input ("ingrese otro valor para el esponente: "))
print("\n")

calculo_potencia = base ** exponente
print(f"El resultado de la potencia es: {calculo_potencia}")
print("=" *100)
print("-" *100)

# ------------------------------Ejecicio 4

import math

print("=" *100)
print("halla la raiz cuadrada solo de los siguientes numeros: 2, 8, 9, 27, 28, 55, 121. \n\n")

numero = int(input("ingrese un numero de los del enunciado para allar su raiz cuadrada: "))
raiz = math.sqrt (numero)
print()
print(f"la raiz cuadrada es: {raiz}")
print("=" *100)
print("-" *100)

# -------------------------------Ejercicio 5

print("=" *100)
nombre_estudiante = input("ingrese su nombre: ")
nota_1 = float(input("ingrese la primera nota: "))
nota_2 = float(input("ingresa la segunda nota: "))
nota_3 = float(input("ingrese la tercera nota: "))
nota_4 = float(input("ingrese la cuarta nota: "))
nota_5 = float(input("ingrese la quinta nota: "))
print("-" *100)

promedio_notas = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5

print(f"El estudiante {nombre_estudiante}, tuvo de promedio en las 5 notas {promedio_notas} ")
print("=" *100)
print("-" *100)

# --------------------------------Ejercicio 6

print("=" *100)
print()

numeroUno = 8
numeroDos = 2

print (f"la variable numeroUno = {numeroUno} y la variable numeroDos = {numeroDos} \n")

numero_Uno = numeroDos
numero_Dos = numeroUno

print(f"Ahora la variable numeroUno = {numero_Uno} y la variable numeroDos = {numero_Dos} \n")

print("=" *100)
print("-" *100)

# --------------------------------Ejercicio 7

print("=" *100)
Esatado = ( 5 == 2 ) or ( 2 > 1 )
