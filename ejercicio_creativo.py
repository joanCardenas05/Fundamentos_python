import random
import time
import os

# ===== LIMPIAR PANTALLA =====
def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

# ===== CARROS DISPONIBLES =====
carros_disponibles = {
    "1": "🚗 Deportivo",
    "2": "🚕 Taxi",
    "3": "🚓 Policía",
    "4": "🏎️ Fórmula 1"
}

# ===== ELEGIR CARRO =====
print("🎮 Elige tu carro:\n")
for clave, nombre in carros_disponibles.items():
    print(f"{clave}. {nombre}")

eleccion = input("\nEscribe el número: ")

if eleccion not in carros_disponibles:
    print("Opción inválida, se asignará uno por defecto")
    eleccion = "1"

carro_jugador = carros_disponibles[eleccion]

# ===== CONFIGURACIÓN =====
meta = 30

# ===== JUGADORES =====
jugadores = {
    f"🧑 Tú ({carro_jugador})": 0,
    "🤖 Rival 1 (🚓)": 0,
    "🤖 Rival 2 (🚕)": 0
}

# ===== DIBUJAR CARRERA =====
def dibujar():
    limpiar()
    print("🏁 ===== CARRERA ===== 🏁\n")

    for nombre, posicion in jugadores.items():
        if posicion > meta:
            posicion = meta

        pista = "-" * posicion + "🏎️" + "-" * (meta - posicion)
        print(f"{nombre}: {pista}")

    print("\nMeta:", " " * meta + "🏁")

# ===== JUEGO =====
input("\nPresiona ENTER para iniciar la carrera...")

ganador = None

while not ganador:
    dibujar()

    for jugador in jugadores:
        avance = random.randint(1, 3)
        jugadores[jugador] += avance

        if jugadores[jugador] >= meta:
            ganador = jugador
            break

    time.sleep(0.3)

# ===== FINAL =====
dibujar()
print(f"\n🏆 ¡GANADOR: {ganador}!")