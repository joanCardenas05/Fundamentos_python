# DESARROLLO DE ACTIVIDAD 1 DE LISTAS EN PYTHON ANDRES CARDENAS

print("=" *100)
print("INVENTARIO DE LA TIENDA ESCOLAR")
print("=" *100 + "\n")

# ------------------------------------------------------------------------------------------

productos = ["cuadernos", "esferos", "lapiz", "borrador", "colores", "blocs"]
precios = [5000.0, 2000.0, 1500.0, 2200.0, 12000.0]
cantidades = [50, 25, 36, 48, 56, 75]

cantidad_productos = len(productos)

# ------------------------------------------------------------------------------------------

print("-" *100)

print("inventario de tienda escolar:"
    "\nproductos:", productos,
    "\nprecios:", precios,
    "\ncantidades:", cantidades,
    "\ncantidad de productos:", cantidad_productos)  

# ------------------------------------------------------------------------------------------

print("-" *100)

print(f"el producto: {productos[0]} tiene un precio de {precios[0]} y una cantidad disponible de {cantidades[0]}")

# ------------------------------------------------------------------------------------------

print("-" *100)

print(type(productos)) # nos muestra el tipo de variabole que es en este caso es una lista

# ------------------------------------------------------------------------------------------

print("-" *100)

print(type(productos[0])) # nos muestra el tipo del primer elemneto de la lista productos en este caso es un string

# ------------------------------------------------------------------------------------------

print("-" *100)