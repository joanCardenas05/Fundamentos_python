# manejo de errores: try-Except

# estructura

try:
    print("intentamos algo")
except:
    print("captura el error")
finally:
    print("esto será ejecutado siendo exitoso o no en el bloque")

# ejemplo: convertir o castear dato de entrada del usuario

try:
    edad_usuario = int(input("ingrese su edad: "))
except ValueError:
    print("bruto hpta ingrese solo numeros ")

# ejemplo: variable indefinida

try:
    print(x)
except NameError: 
    print("Esta vartiable no hasido definida")


# Ejemplo: division por 0

try:
    numero = 10 / 0
except ZeroDivisionError:
    print("no se puede dividir en cero, no sea mula")


