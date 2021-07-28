import random as r

def clave_tarjeta(region):

    letras = "abcdefghijklmnopqrstuvxyz"
    numeros = "1234567890"

    l_letras = list(letras)
    l_numeros = list(numeros)

    lista = l_letras + l_numeros

    clave = []

    for i in range(20):
        resultado = r.choice(lista)
        clave.append(resultado)

    if region == "AMAZONAS":
        clave[9] = "A"
        clave[11] = "M"
        clave.append(clave[3])
        clave.append(clave[5])
        clave.append(clave[7])
        clave = "".join(clave)

    if region == "PUTUMAYO":
        clave[9] = "P"
        clave[11] = "U"
        clave.append(clave[3])
        clave.append(clave[5])
        clave.append(clave[7])
        clave = "".join(clave)

    if region == "CHOCO":
        clave[9] = "C"
        clave[11] = "H"
        clave.append(clave[3])
        clave.append(clave[5])
        clave.append(clave[7])
        clave = "".join(clave)

    if region == "GUAJIRA":
        clave[9] = "G"
        clave[11] = "U"
        clave.append(clave[3])
        clave.append(clave[5])
        clave.append(clave[7])
        clave = "".join(clave)

    if region == "ARAUCA":
        clave[9] = "A"
        clave[11] = "R"
        clave.append(clave[3])
        clave.append(clave[5])
        clave.append(clave[7])
        clave = "".join(clave)

    return clave


region = input("Ingrese el departamento: ")
r_clave = clave_tarjeta(region) # NO BORRAR
print("Esta es su nueva clave:\n")
print(r_clave)
