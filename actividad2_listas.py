print("=" *100)
print("ANALISIS DE TEMPERATURA SEMANALES")
print("=" *100 + "\n")

# ------------------------------------------------------------------------------------------

#   indice negativo          -14 -13 -12 -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
#   indice                    0   1   2   3   4   5   6   7   8   9  10  11  12  13
#   dias                      1   2   3   4   5   6   7   8   9  10  11  12  13  14
temperaturas_registradas = [ 18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18, 20, 22, 19 ]

print("-" *100)
print(f"El primer dia la temperatura fue de {temperaturas_registradas[0]} grados" "\n"
      f"El ultmo dia osea el dia 14, la temperatura fue de {temperaturas_registradas[-1]} grados" "\n"
      f"El septimo dia la temperatura fue de {temperaturas_registradas[-8]} grados" "\n"
      f"Y el penultimo dia osea el dia 13 la temperatura fue de {temperaturas_registradas[12]} grados")

print("-" *100)

print(f"La primera semana hubo estas temperaturas: {temperaturas_registradas[0:7]}" "\n"
      f"La segunda semana hubo estas temperaturas: {temperaturas_registradas[-7:]}" "\n"
      f"solo los dias pares {temperaturas_registradas [1:14:2]}")

temperaturas_registradas.reverse()
print(f"Lista en orden invertido: {temperaturas_registradas}")

print("-" *100)

promedio1 = sum(temperaturas_registradas [0:7] )  / len(temperaturas_registradas [0:7])
print(f"El promedio de la primera semna es: {round(promedio1)} grados")

promedio2 = sum(temperaturas_registradas [7:14] )  / len(temperaturas_registradas [7:14])
print(f"El promedio de la seguda semana es: {round(promedio2)} grados")

