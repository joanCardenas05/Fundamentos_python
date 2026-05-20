# estructura de un diccionario

diccionario = {
    "clave_1" : "valor_1",
    "clave_2" : "valor_2",
    "clave_3" : "valor_3"
}

# diccionario vacio 
dccionarop_vacio = {}

diccionario_aprendiz = {
    "nombre" : "andres",
    "apellido" : "cardenas",
    "programa" : "ADSO",
    "ficha" : "3321349",
    "edad" : 21
}

print(type(diccionario_aprendiz) ) 
# calss <dict>

# obtener un valor del diccionario
print(diccionario_aprendiz["programa"]) 
# ADSO
print(diccionario_aprendiz.get("programa")) 
# ADSO

# obtener solo las claves del diccionario
print(diccionario_aprendiz.keys()) 
# dict_keys(['nombre', 'apellido', 'programa', 'ficha', 'edad'])

# obtener los valores del diccionario
print(diccionario_aprendiz.values()) 
# dict_values(['andres', 'cardenas', 'ADSO', '3321349', 21])

# obtener la clave y el valor 
print(diccionario_aprendiz.items()) 
# dict_items([('nombre', 'andres'), ('apellido', 'cardenas'), ('programa', 'ADSO'), ('ficha', '3321349'), ('edad', 21)])

# agregar un nuevo elememnto al diccionario
diccionario_aprendiz["correo"] = "joanandrescardenas@gamil.com"
print(diccionario_aprendiz.items())
# dict_items([('nombre', 'andres'), ('apellido', 'cardenas'), ('programa', 'ADSO'), ('ficha', '3321349'), ('edad', 21), ('correo', 'joanandrescardenas@gamil.com')])

#  modificar un valor del diccionario
diccionario_aprendiz["programa"] = "SST"
print(diccionario_aprendiz)
# {'nombre': 'andres', 'apellido': 'cardenas', 'programa': 'SST', 'ficha': '3321349', 'edad': 21, 'correo': 'joanandrescardenas@gamil.com'}

# metodo UPDATE (actualizar)
diccionario_aprendiz.update({"nombre":"joan"}) # mdodifica un elemento si existe
diccionario_aprendiz.update({"ciudad":"sogamoso"}) # agrega un nuevo elemento
print(diccionario_aprendiz)
# {'nombre': 'joan', 'apellido': 'cardenas', 'programa': 'SST', 'ficha': '3321349', 'edad': 21, 'correo': 'joanandrescardenas@gamil.com', 'ciudad': 'sogamoso'}

# comprobar pertenencia (in) = COMPROBAR SI UN ELEMENTO EXISTE YA SEA UNA LISTA O TUPLA O DICCIONARIO
if "ficha" in diccionario_aprendiz:
    print("ficha es una de las propiedades de este diccionario") # ficha es una de las propiedades de este diccionario

# recorrer solo las claves del diccionario
for clave in diccionario_aprendiz.keys():
    print(clave) 
"""
nombre
apellido
programa
ficha
edad
correo
ciudad
"""

# recorrer solo los valores del diccionario
for valor in diccionario_aprendiz.values():
    print(valor) 
"""
joan
cardenas
SST
3321349
21
joanandrescardenas@gamil.com
sogamoso
"""

# recorrer las claves y los valores del diccionario 
for clave, valor in diccionario_aprendiz.items():
    print(f"{clave}:{valor}")
"""
nombre:joan
apellido:cardenas
programa:SST
ficha:3321349
edad:21
correo:joanandrescardenas@gamil.com
ciudad:sogamoso    
"""

# Eliminar Elementos en un Diccionario POP()
diccionario_aprendiz.popitem()  # Elimina el ultimo elemento agregado
print(diccionario_aprendiz)
# {'nombre': 'joan', 'apellido': 'cardenas', 'programa': 'SST', 'ficha': '3321349', 'edad': 21, 'correo': 'joanandrescardenas@gamil.com'}

diccionario_aprendiz.pop("edad")  # Elimina un elemento especifico
print(diccionario_aprendiz)
# {'nombre': 'joan', 'apellido': 'cardenas', 'programa': 'SST', 'ficha': '3321349', 'correo': 'joanandrescardenas@gamil.com'}

diccionario_aprendiz.clear()  # Elimina todos los elementos del diccionario
print(diccionario_aprendiz)
# {}


# Diccionarios Anidados
aprendices = {
    "aprendiz_1": {
        "nombre": "Felipe",
        "apellido": "Sandoval",
        "programa": "ADSO",
        "ficha": "33211349",
        "edad": 32
    },

    "aprendiz_2": {
        "nombre": "Camilo",
        "apellido": "Gomez",
        "programa": "SST",
        "ficha": "33211350",
        "edad": 28
    },

    "aprendiz_3": {
        "nombre": "Valentina",
        "apellido": "Lopez",
        "programa": "Topografia",
        "ficha": "33211351",
        "edad": 25
    }
}

# Acceder a un valor en un Diccionario Anidado
print(aprendices["aprendiz_2"]["programa"])  
# SST

# Recorrer un Diccionario Anidado con un ciclo for
for aprendiz, datos in aprendices.items():
    print(f"{aprendiz}:")
    
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")
"""
aprendiz_1:
  nombre: Felipe
  apellido: Sandoval
  programa: ADSO
  ficha: 33211349
  edad: 32

aprendiz_2:
  nombre: Camilo
  apellido: Gomez
  programa: SST
  ficha: 33211350
  edad: 28

aprendiz_3:
  nombre: Valentina
  apellido: Lopez
  programa: Topografia
  ficha: 33211351
  edad: 25 

"""
