# 1. Definición de los conjuntos de aprendices por programa
python_curso = {'Ana', 'Luis', 'Marta', 'Carlos', 'Sofia', 'Pedro'}
java_curso = {'Luis', 'Carlos', 'Pedro', 'Laura', 'Diego'}
bd_curso = {'Marta', 'Sofia', 'Laura', 'Ana', 'Miguel'}

print("=" * 70)
print(f"{'ANALISIS DE MATRICULAS':^70}")
print("=" * 70)


# 2. Operaciones de conjuntos
todos_aprendices = python_curso.union(java_curso, bd_curso)
print(f"1. Total de aprendices únicos (Unión): {len(todos_aprendices)}")
print(f"   Quiénes son: {todos_aprendices}\n")


# -> Aprendices que cursan Python y Java simultáneamente (Intersección)
python_y_java = python_curso.intersection(java_curso)
print(f"2. Aprendices en Python Y Java: {python_y_java}\n")


# -> Aprendices que SOLO están en Python (Diferencia)
solo_python = python_curso.difference(java_curso, bd_curso)
print(f"3. Aprendices SOLO en Python: {solo_python}\n")


# -> Aprendices en exactamente dos programas (Lógica combinada)
# (Intersecciones de a dos, quitando a los que están en las tres)
inter_py_java = python_curso.intersection(java_curso)
inter_py_bd = python_curso.intersection(bd_curso)
inter_java_bd = java_curso.intersection(bd_curso)

triple_inter = python_curso.intersection(java_curso, bd_curso)

exactamente_dos = (inter_py_java | inter_py_bd | inter_java_bd) - triple_inter

print(f"4. Aprendices en EXACTAMENTE dos programas: {exactamente_dos}\n")


# 3. Eliminar duplicados de una lista usando un conjunto
inscripciones = ['Ana', 'Luis', 'Ana', 'Marta', 'Carlos', 'Luis', 'Sofia', 'Pedro', 'Ana']
aprendices_unicos_lista = set(inscripciones)

print("-" * 70)
print(f"5. De la lista de inscripciones, se registraron {len(aprendices_unicos_lista)} únicos.")
print(f"   Quiénes son: {aprendices_unicos_lista}")
print("-" * 70 + "\n")


# Recorre la unión de todos y cuenta en cuántos conjuntos aparece cada nombre
conteo_programas = {
    aprendiz: sum([aprendiz in python_curso, aprendiz in java_curso, aprendiz in bd_curso])
    for aprendiz in todos_aprendices
}

print("6. Conteo de programas por aprendiz (Diccionario por comprensión):")
for nombre, cantidad in conteo_programas.items():
    print(f"   - {nombre}: {cantidad} programa(s)")
print("\n")


# 5. BONUS: Identificar quién está matriculado en los tres programas a la vez
print("-" * 70)
print(f"BONUS - Matriculados en los TRES programas a la vez: {triple_inter if triple_inter else 'Ninguno'}")
print("-" * 70)