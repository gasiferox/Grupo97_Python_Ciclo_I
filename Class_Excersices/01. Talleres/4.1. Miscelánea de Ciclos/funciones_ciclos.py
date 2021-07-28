""" Modulo Ciclos
    Funciones para practicas con ciclos
    Gustavo Romero Nocua
    CC. 79942949
    Mayo 10-2021 """
# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

import math as m
from tabulate import tabulate

def simulador_caida_libre(altura_inicial):

  g = 9.8

  tiempo = m.sqrt((2 * altura_inicial) / g)
  print("El tiempo total es: ",tiempo)
  print(altura_inicial)
  print(g)

  print(tabulate(["t (s)", "altura (m)"], headers="firstrow"))

  i = 0
  while i <= tiempo:
    altura_final = altura_inicial - ((1/2) * g * (i ** 2))
    i += 0.1
    table = [[i,altura_final]]

    #print(altura_inicial,altura_final,i,end=" , ")
    print(tabulate(table))
  return altura_final, i

def generador_generaciones(generacion):
  #generacion = 4
  personas = 1
  poblacion = 1
  i = 0
  print("Generacion: ",i,"Personas: ",personas)
  while i < generacion:
    personas *= 2
    poblacion += personas
    print("Generacion: ",i+1,"Personas: ",personas)
    i += 1
  print("Población: ",poblacion)
  return generacion, personas, poblacion


def constructor_triangulos(pisos):
  pisos = 4
  espacios = "\t\t"
  lineas = "\n\n"
  i = 0
  numero = 0

  for i in range(pisos):
    for j in
  while i < pisos:
    numero += 1
    print([str(numero) + espacios + str(numero + 1) + lineas]*3)
    i += 1
  return "No implementada aún"

triangulo = constructor_triangulos(4)

def constructor_tableros(longitud):
  #TODO Comentar código
  #TODO Implementar la función
  return "No implementada aún"
