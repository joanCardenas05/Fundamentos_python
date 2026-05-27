# Lista de canciones
cancionesFavoritas = ["ROADS UNTRAVELED","CARRIE","LIKE A STONE","NOVEMBER RAIN","MY FAVORITE GAME"]
print(f"Canciones favoritas: {cancionesFavoritas}")

# Cancion nueva agregada al final
cancionesFavoritas.append("MAGIC")
print(f"La cancion del final cambio {cancionesFavoritas}")

# Cancion nueva agregada de segundas
cancionesFavoritas.insert(2, "SHOOT TO THRILL")
print(f"La segunda cancion se cambio {cancionesFavoritas}")

# Estamos combinando 2 listas
bonusTrack = ["BonusTrack 1", "Bonus Track 2"]
cancionesFavoritas.extend(bonusTrack)
print(f"La lista se combino con bonusTrack {cancionesFavoritas}")

# Remover una cancion
cancionesFavoritas.remove("CARRIE")
print(f"Se removio una cancion {cancionesFavoritas}")

# Eliminar la ultima cancion
cancionesFavoritas.pop()
print(f"Se elimino la ultima cancion {cancionesFavoritas}")

# Lista ordenada
cancionesFavoritas.sort()
print(f"Lista ordenada alfabeticamente {cancionesFavoritas}")

# preguntas
"""
¿Cuantas canciones tiene la playlist?
"""

print(len(cancionesFavoritas))

"""
¿En qué posición está la primera canción que agregaste?
"""

posicion = cancionesFavoritas.index("NOVEMBER RAIN")
print(f"La posicion de la primera cancion que agregue fue {posicion}")

"""
¿Cuantas veces aparece el string 'Bonus Track 1'?
"""

veces = cancionesFavoritas.count("BonusTrack 1")
print(f"Aparece las siguientes veces {veces}")


