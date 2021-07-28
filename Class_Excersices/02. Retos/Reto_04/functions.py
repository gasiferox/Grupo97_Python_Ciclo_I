import random

def clave_tarjeta(region):

    letras = "abcdefghijklmnopqrstuvxyz"
    numeros = "1234567890"
    amazonas = "AMAZONAS"
    choco = "CHOCO"
    guajira = "GUAJIRA"
    arauca = "ARAUCA"
    putumayo = "PUTUMAYO"

    l_letras = list(letras)
    l_numeros = list(numeros)
    l_amazonas = list(amazonas)
    l_choco = list(choco)
    l_guajira = list(guajira)
    l_arauca = list(arauca)
    l_putumayo = list(putumayo)

    lista_clave = l_letras + l_numeros
    clave = []

    for i in range(20):
        resultado = random.choice(lista_clave)
        clave.append(resultado)

    if region == "AMAZONAS":
        lista_region = l_amazonas[0:2]
        clave[9] = lista_region[0]
        clave[11] = lista_region[1]
        verificacion = clave[3:8:2]
        clave = clave + verificacion
        clave = " ".join(clave)
    elif region == "CHOCO":
        lista_region = l_choco[0:2]
        clave[9] = lista_region[0]
        clave[11] = lista_region[1]
        verificacion = clave[3:8:2]
        clave = clave + verificacion
        clave = " ".join(clave)
    elif region == "GUAJIRA":
        lista_region = l_guajira[0:2]
        clave[9] = lista_region[0]
        clave[11] = lista_region[1]
        verificacion = clave[3:8:2]
        clave = clave + verificacion
        clave = " ".join(clave)
    elif region == "ARAUCA":
        lista_region = l_arauca[0:2]
        clave[9] = lista_region[0]
        clave[11] = lista_region[1]
        verificacion = clave[3:8:2]
        clave = clave + verificacion
        clave = " ".join(clave)
    elif region == "PUTUMAYO":
        lista_region = l_putumayo[0:2]
        clave[9] = lista_region[0]
        clave[11] = lista_region[1]
        verificacion = clave[3:8:2]
        clave = clave + verificacion
        clave = " ".join(clave)

    return clave

def header_main(title):
    print("#"*(len(title)+7))
    print("#\t"+title+"\t#")
    print("#"*(len(title)+7))
    print("")
