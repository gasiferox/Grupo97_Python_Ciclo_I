""" RETO 2
    FUNCIONES PARA EJECUTAR EL PROGRAMA QUE GENERA UNA DIRECCIÓN DE CORREO
    A PARTIR DE LOS DATOS DEL USUARIO

    Gustavo Romero Nocua
    gasifero@gmail.com
    Junio 15-2021 """

def generar_correo(nombre,apellido,agnio_nacimiento,opcion)->str:

    CORREO="@misiontic.com"

    if opcion == 1:
        nuevo_correo = nombre[0:1] + apellido[0:1] + CORREO
    elif opcion == 2:
        nuevo_correo = nombre[0:3] + apellido[0:2] + CORREO
    elif opcion == 3:
        nuevo_correo = nombre[0:3] + apellido[len(apellido)-2:] + str(agnio_nacimiento) + CORREO

    return nuevo_correo

def comprobar_nombre(nombre):

    if nombre.isalnum():
        nombre = nombre.lower()

    else:
        print("El nombre no cumple con los parámetros")
        nombre = input("Por favor ingrese su nombre de nuevo: ")
        nombre = nombre.lower()

    return nombre

def comprobar_apellido(apellido):

    if apellido.isalnum():
        apellido = apellido.lower()

    else:
        print("El apellido no cumple con los parámetros")
        apellido = (input("Por favor ingrese su apellido de nuevo:"))
        apellido = apellido.lower()

    return apellido

def comprobar_agnio_nacimiento(agnio_nacimiento):

    if str(agnio_nacimiento).isnumeric() and agnio_nacimiento >= 1901 and agnio_nacimiento <= 2020:
        agnio_nacimiento = agnio_nacimiento
    else:
        print("El año ingresado no corresponde con un valor válido")
        agnio_nacimiento = (input("Ingrese el año nuevamente: "))

    return agnio_nacimiento

def comprobar_opcion(opcion):

    if opcion >= 1 and opcion <= 3:
        pass
    else:
        print("La opción seleccionada no es válida")
        opcion = print(input("Ingrese la opción nuevamente: "))

    return opcion

def header_main(title):

    print("#"*(len(title)+7))
    print("#\t"+title+"\t#")
    print("#"*(len(title)+7))
    print("")

def options_main():
    print("\n## O P C I O N E S ##\n")
    print("A continuación las opciones para crear su cuenta de correo, por favor seleccione una.\n")
    print("1. inicial_nombre+inicial_apellido1@misiontic.com")
    print("2. primeras_3_letras_nombre+primeras_2_letras_apellido@misiontic.com")
    print("3. primeras_3_letras_nombre+ultimas_2_letras_apellido+fecha_nacimiento@misiontic.com")
    print("\tNota: El (+) no hace parte de la dirección de correo\n")
