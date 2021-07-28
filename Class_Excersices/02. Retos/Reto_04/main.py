import functions as f

f.header_main(title="Reto 5")

region = str(input("Ingrese la región a la cual pertenece: "))

clave = f.clave_tarjeta(region)

print("La clave asignada es:\n", clave)
