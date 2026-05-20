print("=" *45)
print("            Clasificador de IMC")
print("=" *45)
print()

peso = float(input("Ingrese su peso en kg.: "))
estatura = float(input("Ingrese su estatura en m.: "))
imc = peso / (estatura ** 2)

if (peso <= 0 or estatura <= 0):
    print("no es valido el valor menor que cero")
    print("por favor ingrese su estatura o peso real 😊")

elif imc < 18.5:
    print("=" *45)
    print("ESTAS BAJO DE PASO 😥")
    print("-" *45)
    print("Estado:  ⚪")
    print("=" *45) 
elif imc >= 18.5 and imc <= 24.9:
    print("=" *45)
    print ("ESTAS EN EL PESO IDEAL 🤩")
    print("-" *45)
    print("Estado:  🟢")
    print("=" *45)
elif imc >= 25 and imc <= 29.9:
    print("=" *45)
    print("ESTAS EN SOBRE PESO, MEJORAR LA DIETA 🥗")
    print("-" *45)
    print("Estado:  🟡")
    print("=" *45)
elif imc >= 30 :
    print("=" *45)
    print("ESTAS EN OBESIDAD, BUSCA AYUDA PROFESIONAL ☠️")
    print("-" *45)
    print("Estado:  🔴")
    print("=" *45)
else:
    print("=" *45)
    print("¡¡INGRESA UN NUMERO VALIDO!!")
    print("=" *45)
