import funciones_ciclos as fc

altura_inicial = 50
altura_final = fc.simulador_caida_libre(altura_inicial)

generacion = int(input("Ingrese el numero de generaciones a consultar: "))
poblacion, generacion, personas = fc.generador_generaciones(generacion)


