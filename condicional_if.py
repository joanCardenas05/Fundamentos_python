# if encadenado

edad = int(input("¿cual es tu edad?"))

if edad < 18:
    print("Eres un menor de edad")
elif edad >= 18 and edad < 65:
    print("Eres una persona responsable")
else : 
    print("Eres un adulto mayor")


# id anidado

edad = int(input("Cual es tu edad?"))

if edad < 18:
    if edad >= 12 and edad < 18:
        print("adolescente")
    else: 
        print("niño")
else:
    if edad > 18 and edad <=60:
        print("Eres un adulto")
    elif edad > 90:
        print("ya te muriste")
    else:
        print("Eres un adulto mayor")

# operador ternario

numero = 4

if numero % 2 == 0:
    print("El numero es par")
else: 
    print("El numero es impar")


number = 4

print("El numero es par") if numero % 2 == 0 else print("El numero es impar ")

