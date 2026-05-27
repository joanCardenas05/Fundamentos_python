# 2. Función para calcular el promedio de notas
def calcular_promedio(lista_notas):
    # Recibe una lista de 4 floats y retorna el promedio.
    if not lista_notas:
        return 0.0
    return sum(lista_notas) / len(lista_notas)


# 1. Creación del diccionario 'grupo' con los primeros 4 aprendices
grupo = {
    3321349: {
        "nombre": "Andres Cardenas",
        "edad": 21,
        "notas": [4.5, 5.0, 4.2, 4.0],
        "ciudad": "sogamoso"
    },

    2567489: {
        "nombre": "Ana Maria Gomez",
        "edad": 19,
        "notas": [3.0, 2.8, 3.5, 2.5],
        "ciudad": "Sogamoso"
    },

    2890123: {
        "nombre": "Carlos Mendoza",
        "edad": 24,
        "notas": [4.8, 4.9, 4.7, 5.0],
        "ciudad": "Tunja"
    },

    3123456: {
        "nombre": "Luisa Fernanda Restrepo",
        "edad": 22,
        "notas": [2.5, 3.0, 1.5, 3.2],
        "ciudad": "Duitama"
    }
}


# 4. Modificaciones al diccionario después de crearlo
# -> Agregar un nuevo aprendiz usando una nueva clave de ficha
grupo[3456789] = {
    "nombre": "Diego Alexander Pérez",
    "edad": 20,
    "notas": [4.0, 4.1, 3.9, 4.3],
    "ciudad": "Villa de Leyva"
}

# -> Actualizar la ciudad de uno de los aprendices existentes
grupo[3123456]["ciudad"] = "Bogotá"


# 3. Generar el reporte base usando .items() y un ciclo for
print("-" * 75)
print(f"{'REPORTE GENERAL DE APRENDICES':^75}")
print("-" * 75)
print(f"{'Ficha':<10} | {'Nombre':<22} | {'Edad':<4} | {'Promedio':<8} | {'Estado':<10}")
print("-" * 75)

for ficha, datos in grupo.items():
    promedio = calcular_promedio(datos["notas"])

    # Determinar estado según la condición (promedio >= 3.0)
    estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"

    print(f"{ficha:<10} | {datos['nombre']:<22} | {datos['edad']:<4} | {promedio:<8.2f} | {estado:<10}")

print("-" * 75)
print("\n")


# 5. BONUS: Ordenar de mayor a menor promedio usando sorted() con key=
print("-" * 75)
print(f"{'BONUS: APRENDICES ORDENADOS POR PROMEDIO (MAYOR A MENOR)':^75}")
print("-" * 75)
print(f"{'Ficha':<10} | {'Nombre':<22} | {'Promedio':<8} | {'Ciudad':<15}")
print("-" * 75)

# Convertimos los items a una lista para ordenarla.
# La clave (key) accede al diccionario interno, calcula el promedio y reverse=True ordena descendente.
grupo_ordenado = sorted(
    grupo.items(),
    key=lambda item: calcular_promedio(item[1]["notas"]),
    reverse=True
)

for ficha, datos in grupo_ordenado:
    promedio = calcular_promedio(datos["notas"])

    print(f"{ficha:<10} | {datos['nombre']:<22} | {promedio:<8.2f} | {datos['ciudad']:<15}")

print("-" * 75)

