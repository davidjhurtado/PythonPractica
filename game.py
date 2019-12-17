#### JUEGO DE ANDRES####
print ("Hola...")
print("Bienvenido a mi juego")
nb = input("Escribe algo:")
nombre = ""
resp = nb.upper()
if resp == "TOC TOC" or resp == "HOLA":
    nombre = input("Quién es?")
else:
    print (resp )
if nombre == "Andres":
    edad = input("Qué edad tienes?")
    print ("Que Cool " + nombre + " Te filicito...")
else:
    if nombre == "Arturo":
        print (nombre + " Eres muy locoococococococo".upper())
