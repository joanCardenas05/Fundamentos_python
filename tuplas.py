# Tuplas

# Estructura de una tupla

tupla = ("elemennto_1", "elemento_2", "elemennto_3")
print(type(tupla))

tupla2 = "a", "b", "c"
print(type(tupla2))

tupla3 = ("hola",)
print(type(tupla3))

tupla4 = tuple("Hola",)
print(tupla4)

tuplas_mixtas = ("hola", 1 , 3.14, [1,2,3],(4,5,6))
print(tuplas_mixtas)

# Tupla aprendices adso

aprendices = ("andres","camilo", "juan","manuela")
print(aprendices)

# Acceder a un elementos de la tupla
print(aprendices[0])

# Modificar un elemento de la tupla
# aprendices[0] = "andres" 
# Esto no se puede hacer porque las tuplas son inmutables

# consultar rangos de elementos de la tupla
print(aprendices[0:2])
print(aprendices[1:4])
print(aprendices[1:])

# sumar dos tuplas
tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla_suma = tupla1 + tupla2
print(tupla_suma)

# multiplicar una tupla
tupla_multiplicada = tupla1 * 3
print(tupla_multiplicada)

# Metodos de las tuplas
print(len(aprendices)) # 5

# Contar cuantas veces aparece un elemento en la tupla
print(aprendices.count("andres")) # 1

# Encontrar el indice de un elemento en la tupla
print(aprendices.index("juan")) # 2

# Modificar una tupla a lista
print(type(aprendices)) # class tuple
aprendices_lista = list(aprendices)
print(type(aprendices_lista)) # class list

aprendices_lista.append("santiago")
print(aprendices_lista)

aprendices = tuple(aprendices_lista) # Convertir la lista de nuevo a tupla
print(aprendices)

#  Comprobar pertenece a una tupla
print("santiago" in aprendices) # True
print("maria" in aprendices) # False

# Empaquetar tuplas

programa_1  = "ADSO"
programa_2 = "SST" 
programa_3 = "Topografia"

tupla_programas = (programa_1, programa_2, programa_3)
print(tupla_programas)

# Desempaquetar tuplas
tupla_desempaquetada = ("ADSO", "SST", "Topografia")
programa_1, programa_2, programa_3 = tupla_desempaquetada
print(programa_1) # ADSO

# Ejercicio 2 desempaquetar tuplas
tupla_cuidades = ("Bogota", "Medellin", "Cali", "Barranquilla", "Cartagena")
ciudad_1, *ciudad_2 = tupla_cuidades
print(ciudad_1) # Bogota
print(ciudad_2) 

for holaa in tupla_cuidades:
    print(holaa)