""" Programa para apoyar al marinero Seijo
    Gustavo Romero Nocua
    gasifero@gmail.com
    CC. 79942949
    Junio 18-2021 """

import utilidades as util

criaturas = util.aparecer_criatura()
direccion = util.aparecer_direccion()


util.header_main(title="4.0 - Ahoy! Capitan")
print("Aparicion: ",criaturas)
print("Dirección: ",direccion)
print("")
articulo_criatura, articulo_direccion = util.grito_marinero(criaturas, direccion)
util.imprime_grito(articulo_criatura, criaturas, articulo_direccion, direccion)
