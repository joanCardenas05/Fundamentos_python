# open (nombre del archivo) -> Funcion de python para manipular archivos 

# r (Read) lectura
# w (Write) Escritura     # siempre se debe escribir la lettra en minuscula porque en mayuyscula no funciona
# x (Crear Archivo Nuevo)
# a (Add) Escibir nuevo texto

try:
    file = open("archivos.txt", "r")
    print(file.readline()) # Lee la primera linea 
    file.close() # ciera el archivo para que no robe informacion
except FileNotFoundError:
    print("No se encontro el archivo")


# Uso del WITH para no cerrar el archivo manualmente

try:
    with open("archivos.txt", "r") as file:
        print(file.readline())
except FileNotFoundError:
    print("No se encontro el archivo")

# Sobrescribir un Archivo del sistema

try:
    with open("archivo.txt", "w") as file:
        file.write("texto sobrescrito") # sobrescribe
except FileNotFoundError:
    print("No se encontro el archivo")

# Escribir un texto nuevo en un archivo del sistema

try:
    with open("archivo.txt", "a") as file:
        file.write("\nNuevo texto") # escribe
    with open("archivo.txt", "r") as file:
        print(file.read()) # lee
except FileNotFoundError:
    print("No se encontro el archivo")


# creacion de un archivo del sistema

try:
    with open("archivo_2.txt", "r") as file:
        print(file.readline())
except FileNotFoundError:
    open("archivo_2.txt", "x") # cree un nuevo archivo
    print("No se encontro un archivo ")


# Creacion de un archivo HTML en el Sistema:
def crear_archivo_html(script_html):
    try:
        with open("pagina_2.html", "r") as file:
            print(file.readline())
    except FileNotFoundError:
        open("pagina_2.html", "x")  # Cree un nuevo archivo
        print("No se encontro el archivo")


    # Escribir el codigo HTML nuevo en un Archivo del Sistema:
    try:
        with open("pagina_2.html", "a") as file:
            file.write(script_html)  # Escribe

        with open("pagina_2.html", "r") as file:
            print(file.read())  # Lee

    except FileNotFoundError:
        print("No se encontro el archivo")


crear_archivo_html("<html> <body><h1>Hola soy un virus nuevo</h1> </body> </html>")

