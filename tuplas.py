tupla_desempaquetada = ("ADSO", "SST", "Topografia")
programa_1, programa_2, programa_3 = tupla_desempaquetada

print(programa_1)
print(programa_2)
print(programa_3)

tupla_ciudades = ("bogota", "medellin", "cali")
ciudad_1, *ciudad_2 = tupla_ciudades

print(ciudad_1)
print(ciudad_2)

# iterar una tuppla con un ciclo for

for ciudad in tupla_ciudades:
    print(ciudad)

