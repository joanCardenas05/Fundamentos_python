print("Hello World")

# --------------------------------------------------------

nombre_aprendiz = "Andres Cardenas"

print(nombre_aprendiz)

# --------------------------------------------------------

x = "Esta es un  x minuscula"
print(x)

X = "Esta es una x mayuscula"
print(X)

# --------------------------------------------------------

nombre = "Andres"
apellido = "Cardenas"
edad = 21
altura = 1.80
activo = True
correo = "joanandrescardenas@gmail.com"
telefono = "313512288"
cedula = 1057573697 

# ---tipo de casteo(casting) = cambiar el tipo de dato----

telefono_entero = int(telefono)
edad_flotante = float(edad)
altura_entero = int(altura)
cedula_string = str(cedula)

# --------------------------------------------------------

print(type(nombre), nombre)
print(type(apellido), apellido)
print(type(edad), edad)
print(type(altura), altura)
print(type(activo), activo)
print(type(correo), correo)
print(type(telefono), telefono)
print(type(cedula), cedula)

# --------------------------------------------------------

print(type(telefono_entero), telefono_entero)
print(type(edad_flotante), edad_flotante)
print(type(altura_entero), altura_entero)
print(type(cedula_string), cedula_string)

# --------------------------------------------------------

# print(telefono_entero)

# print("soy", nombre, apellido, "tengo", edad, "mido", altura, "mi correo es", correo, "y mi numero es", telefono)

# ---------------------indentacion-------------------------

if 5 > 2:
    print("5 es mayor que 2")

else:
    print("5 no es mayor que 2")

# ----------------------input------------------------------

name = input("¿cual es tu nombre?")
print(name)

years_old = int(input("ingrese su edad:"))
print(type(years_old),years_old)

if years_old >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

print(f"Hola {name}, tienes {years_old} Años")



