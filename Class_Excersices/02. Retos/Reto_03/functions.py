""" RETO 3
    FUNCIONES PARA EJECUTAR EL PROGRAMA QUE GENERA UNA DIRECCIÓN DE CORREO
    A PARTIR DE LOS DATOS DEL USUARIO

    Gustavo Romero Nocua
    gasifero@gmail.com
    
    Junio 15-2021 """

def header_main(title):

    print("#"*(len(title)+7))
    print("#\t"+title+"\t#")
    print("#"*(len(title)+7))
    print("")

def clave_segura(clave):

    mensaje = None

    if len(clave) >= 6 and len(clave) <= 12:
        longitud = True
    else:
        print("La longitud no cumple con las condiciones")
        longitud = False

    for caracteres in clave:

        minusculas = False
        if caracteres.islower():
            minusculas = True
            break

    for caracteres in clave:

        mayusculas = False
        if caracteres.isupper():
            mayusculas = True
            break

    for caracteres in clave:

        numero = False
        if caracteres.isnumeric():
            numero = True
            break

    for caracteres in clave:

        alfanum = False
        if caracteres.isalnum():
            alfanum = True
            break

    for caracteres in clave:

        espacio = False
        if caracteres.isspace():
            espacio = True
            break

    for caracteres in clave:

        caracter_esp = False
        if caracteres.find("#") != -1:
            caracter_esp = True
            break

    if longitud == True and minusculas == True and mayusculas == True and numero == True and alfanum == True and espacio == False and caracter_esp == True:
        mensaje = "CORRECTO"
    else:
        mensaje = "INCORRECTO"

    #print("longitud ",longitud,"\nmayusculas ",mayusculas, "\nminusculas ", minusculas, "\nnumero ", numero, "\nalfanum ",alfanum, "\nespacio ", espacio, "\ncaracter_esp",caracter_esp)

    return mensaje
