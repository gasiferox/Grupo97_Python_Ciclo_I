n = int(input("Ingrese un valor: "))
nombre_archivo = "tabla" + str(n) + ".txt"

f = open(nombre_archivo, "w")

for i in range(0,10):
    f.write(str(i)+str(n)+"hola"+"\t")
f.close()
