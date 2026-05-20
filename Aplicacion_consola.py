import random

print("🎮 Bienvenido al juego de adivinar el número")

# ===== CONFIGURACIÓN =====
numero_secreto = random.randint(1, 100)
intentos = 0
max_intentos = 7

print("\nHe pensado un número entre 1 y 100")
print(f"Tienes {max_intentos} intentos")

# ===== JUEGO =====
while intentos < max_intentos:
    intento = input("\nAdivina el número: ")

    # Validar que sea número
    if not intento.isdigit():
        print("❌ Escribe un número válido")
        continue

    intento = int(intento)
    intentos += 1

    if intento == numero_secreto:
        print(f"\n🎉 ¡Correcto! Adivinaste en {intentos} intentos")
        break

    elif intento < numero_secreto:
        print("🔽 Muy bajo")

    else:
        print("🔼 Muy alto")

    print(f"Intentos restantes: {max_intentos - intentos}")

# ===== FINAL =====
if intento != numero_secreto:
    print(f"\n💀 Perdiste. El número era {numero_secreto}")