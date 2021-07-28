""" RETO 2
    PROGRAMA PARA CREAR CORREOS A PARTIR DE 3 OPCIONES TOMANDO LOS DATOS DEL USUARIO

    Gustavo Romero Nocua
    gasifero@gmail.com
    CC. 79942949
    Junio 15-2021 """

import functions as f

title = "RETO 2 - Concatenación de Cadenas"
header = f.header_main(title)

nombre = str(input("Indique su nombre: "))
nombre = f.comprobar_nombre(nombre)

apellido = str(input("indique su apellido: "))
apellido = f.comprobar_apellido(apellido)

agnio_nacimiento = int(input("Indique el año de nacimiento: "))
agnio_nacimiento = f.comprobar_agnio_nacimiento(agnio_nacimiento)


options_main = f.options_main()

opcion = int(input("Indique la opción de su preferencia (1 - 3): "))
opcion = f.comprobar_opcion(opcion)

print("\nEl correo del usuario es el siguiente:\n")

nuevo_correo = f.generar_correo(nombre, apellido, agnio_nacimiento, opcion)
print(nuevo_correo)
