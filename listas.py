# listas 

# estructura de una lista 

# indice:         0         1        2          3         4  
#indice_negativo  -4       -3       -2         -1         0
aprendices = ["camilo", "simon", "santiago", "leonardo", "Stefy"]
print(aprendices)

# # acceder a un elemento de la lista 
print(aprendices [1]) 

# modificar un elemento de lista 
aprendices[2] = "Andres"
print(aprendices) # cambio a santiago por andres

# consultar renagos de elementos de la lista 
print(aprendices[0:2]) # [camilo, simon]
print(aprendices[:2]) # [camilo, simon]
print (aprendices[2:5]) #[santiago, andres, stefy]
print (aprendices[2:]) #[santiago, andres, stefy]
print (aprendices[2:2]) #[] no aparece nada por que lo excluye 
print (aprendices[:]) #

lista_mixta = ["hola", 1, 3.14, True, {1,2,3,3,} ]

# concatenar listas

ficha_3321349 = ["andres", "stephanie", "camilo", "ronalt", "stevent", "simon"]
ficha_2993648 = ["andres","gabrile", "mario", "alberto", "rogelio", "maria"]

fichas_ADSO = ficha_3321349 + ficha_2993648

print(fichas_ADSO)

# unir listas con extend

ficha_3321349.extend(ficha_2993648)
print(ficha_3321349)


# medir el largo de las listas con len() 
longitud_ADSO = len(fichas_ADSO)
print(f"la lista de aprendices ADSO tiene {longitud_ADSO} elementos.")

# print(len(fichas_ADSO)) #12



# contar elementos repetidos con count  
count_andres = fichas_ADSO.count("andres")
print(f"el nombre andres aparece {count_andres} veces en la lista.")


# obtener el indice con un elemento con index 

indice_alberto = fichas_ADSO.index("alberto")
print(f"el nomnbre de alberto se encuentra en el inidice {indice_alberto}.")


# copiar una lista con copy

copia_lista_fichas_ADSO = fichas_ADSO.copy()
print(copia_lista_fichas_ADSO)


#  Agregar elementos (append e insert) 

copia_lista_fichas_ADSO.append("falcao") # agrega al final de la lista
print(copia_lista_fichas_ADSO)

copia_lista_fichas_ADSO.insert(0, "james") # se agrega en la posicion que le demos 
print(copia_lista_fichas_ADSO)


# eliminar elementos con (remove y pop)

copia_lista_fichas_ADSO.remove("andres") # elimina por valor y como esta repetido borrr el primero que encuentra
print(copia_lista_fichas_ADSO)

copia_lista_fichas_ADSO.pop(3) # borra el elemento por el indice especifico
print(copia_lista_fichas_ADSO) 


# comprobar pertenecia (in) es para validar si algun elemento que bsuquemos este 

if "falcao" in copia_lista_fichas_ADSO:
    print("falcao si esta en la lista de copia de fichas de ADSO")

else:
    print("falcao no esta en la lista de ADSO")


#  ordenar (sort() o reverse())

copia_lista_fichas_ADSO.sort() # ordena la lista en orden alfabetica
print(copia_lista_fichas_ADSO)

copia_lista_fichas_ADSO.reverse() # invierte el orden de la lista
print(copia_lista_fichas_ADSO)

# lista_mixta.sort() # esto no se puede ordenar porque no se pueden mezclar diferentes tipos de elementos
# print(lista_mixta)

# copia_lista_fichas_ADSO.clear() # elimina todos los elementos de la lista 
# print(copia_lista_fichas_ADSO)
