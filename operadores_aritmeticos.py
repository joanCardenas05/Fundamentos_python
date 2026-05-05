# OPERADORES ARITMETICOS
a = 50
b = 20 
# SUMA
suma = a + b
print (f"La suma de {a} y {b} es: {suma}")

# RESTA
resta = a - b
print (f"La resta de {a} y {b} es: {resta}")

# MULTIPLICACION
multiplicacion = a * b
print (f"La multiplicacion de {a} y {b} es: {multiplicacion}")
# DIVISION DECIMAL
division = a / b
print (f"La division de {a} y {b} es: {division}")
# DIVISION ENTERA
division_entera = a // b
print (f"La division entera de {a} y {b} es: {division_entera}")

# MODULO o residuo de la division
modulo = a % b
print (f"El modulo de {a} y {b} es: {modulo}")
# POTENCIA
potencia = a ** b
print (f"La potencia de {a} y {b} es: {potencia}")

# precedencia de operadores
resultado = a + b * 2
print (f"El resultado de la operacion es: {resultado}")
resultado_2 = (a + b) * 2
print (f"El resultado de la operacion es: {resultado_2}")
resultado_3 = a*b //3
print (f"El resultado de la operacion es: {resultado_3}")
resultado_4 = (a * b) // 3
print (f"El resultado de la operacion es: {resultado_4}")
resultado_5 = a * (b // 3)
print (f"El resultado de la operacion es: {resultado_5}")

ejercicio_s =  (a*(a+b)/b) *(a-b) +(a*b) - (a/b)
print (f"El resultado del ejercicio es: {ejercicio_s}")

# librerias de matematicas 
import math


print(math.pi)
print(math.e)
print(math.sqrt(16))


import random # LIBRERIA PARA GENERAR NUMEROS ALEATORIOS

random.random()
numero_aleatorio = random.randint(1, 10)
print(f"El numero aleatorio generado es: {numero_aleatorio}")