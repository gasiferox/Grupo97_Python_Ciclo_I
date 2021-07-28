""" Programa Apoyo multas#
    incorpora al modulo multas.py
    Gustavo Romero Nocua
    gasifero@gmail.com
    Junio 11-2021 """

#---------------- Zona librerias------------
import multas as mult

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

distancia_uno = float(input("Distancia 1 (metros): "))
distancia_dos = float(input("Distancia 2 (metros): "))
tiempo = float(input("Tiempo (segundos): "))
grado_alcohol = float(input("Grado de alcohol en la sangre: "))


multa_velocidad, velocidad = mult.multar_velocidad(distancia_uno,distancia_dos,tiempo)

multa_alcoholemia = mult.multar_alcoholemia(grado_alcohol)

print("\n\nLa velocidad del vehículo es de",velocidad,"km/h, \nel estado del conductor respecto al transito es\n",multa_velocidad,".\n\nEl grado de alcohol reportado fue de",grado_alcohol,"mg de etanol/100 ml, \npor lo cual se encuentra",multa_alcoholemia,".")
