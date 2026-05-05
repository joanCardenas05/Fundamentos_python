print("=" *45)
print("           CALCULADORA DE ANDRES")
print("=" *45)

valor_uno = float(input("Ingrese el primer valor:"))
valor_dos = float(input("Ingrese el segundo valor:"))
tipo_de_operacion = int(input("ingrese el numero de la operacion que desea realizar: \n 1.suma \n 2.resta \n 3.multiplicacion \n 4.division \n" ))


suma = valor_uno + valor_dos
resta = valor_uno - valor_dos
multiplicacion = valor_uno * valor_dos
# division = valor_uno / valor_dos

if tipo_de_operacion == 1:
    print("El resultado es:", suma)

elif tipo_de_operacion == 2:
    print("El resultado es:", resta)

elif tipo_de_operacion == 3:
    print("El resultado es:", multiplicacion)

elif tipo_de_operacion == 4:
    if valor_dos != 0:
        division = valor_uno / valor_dos
        print("El resultado es:", division)
    else: 
        print("Error: No se puede dividir en cero")
else:
    print("Operacion no valida")


