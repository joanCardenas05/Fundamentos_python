valor_uno = float(input("Ingrese el primer valor:"))
valor_dos = float(input("Ingrese el segundo valor:"))
tipo_de_operacion = int(input("ingrese el numero de la operacion que desea realizar: \n 1.suma \n 2.resta \n 3.multiplicacion \n 4.division \n" ))


suma = valor_uno + valor_dos
resta = valor_uno - valor_dos
multiplicacion = valor_uno * valor_dos
division = valor_uno / valor_dos

if tipo_de_operacion == 1:
    print("El resultado es:", suma)

if tipo_de_operacion == 2:
    print("El resultado es:", resta)

if tipo_de_operacion == 3:
    print("El resultado es:", multiplicacion)

if tipo_de_operacion == 4:
    print("El resultado es:", division)

# print(f "{}")
