n = int(input("Ingrese el valor del archivo: "))
m = int(input("Ingrese el numero de la linea que quiere leer: "))

archivo_nombre = "tabla" + str(n) + ".txt"

try:
    f = open(archivo_nombre, "r")
except FileNotFoundError:
    print("El archivo no existe")
else:
    linea = f.readlines()
    print(linea[m-1])
