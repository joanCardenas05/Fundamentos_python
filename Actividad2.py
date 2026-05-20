print("=" *45)
print("        CALCULADORA DE NOTAS ANDRES")
print("=" *45)
print()

nota_maxima = 5.0
nota_minima = 0.5
nota_1 = float(input("Ingrese la primera NOTA: "))
nota_2 = float(input("Ingrese la segunda NOTA: "))
nota_3 = float(input("Ingrese la tercera NOTA: "))
print("\n")

# -------------------calcula el promedio sumando y dividiendo------------------------------ 

promedio = (nota_1+ nota_2+nota_3)/3

# ---------------------resultado promedio ---------------

print("=" *8 , "promedio", "=" *8 )
print("=" *45)
print(f" el promedio del estudiante es: {round(promedio, 2)}" )
print("=" *45)
print("\n")

# ---------puntos que faltan para la maxima nota-------

puntos_faltantes = nota_maxima - promedio

print("=" *8 , "FALTANTE PARA NOTA MAXIMA", "=" *8 )
print("=" *45)
print(f"Al aprendiz le hacen falta: {round(puntos_faltantes, 2)}" )  #el round aca redondea a solo 2 decimales 
print("=" *45)
print()



# ----------------limitar valores---------------

# ----------- APROBADO O NO APROBADO ------------------
if promedio >= 3.0:

    if promedio >= 3.0 and promedio < 4.0:
        print("APROBADO 👍")
    elif promedio >= 4.0 and promedio <= 4.5:
        print("SUPERIOR ✔️")
    else:
        print("SOBRESALIENTE ✅")
    
else:
    print("NO APROBADO ❌")

print("\n")



