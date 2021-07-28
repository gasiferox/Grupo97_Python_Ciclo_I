""" RETO 3
    PROGRAMA PARA VALIDAR CLAVES DE USUARIO Y DETERMINAR SI SON SEGURAS

    Gustavo Romero Nocua
    gasifero@gmail.com
    
    Junio 18-2021 """


import functions as f

title = "Reto 3 - Cadenas - Verificar Contraseña"
f.header_main(title)

clave = input("Ingrese la clave: ")

mensaje = f.clave_segura(clave)

print("El resultado del análisis de la clave es: " + mensaje)
