""" Modulo generador aleatorio de cadenas #
    Funciones que retornan criaturas marinas
    y ubicaciones del barco
    Gustavo Romero Nocua
    gasifero@gmail.com
    Junio 18-2021 """

import random
# Definición de Funciones
def aparecer_criatura():
  criaturas=["Kraken","Sirenas","Ballena","Hipocampo","Macaraprono","Pulpo","Leviatanes","Hidras"]
  indice = random.randint(0, 7)
  return criaturas[indice]

def aparecer_direccion():
  direccion=["babor","estribor","proa","popa"]
  indice = random.randint(0, 3)
  return direccion[indice]

def imprimir_aparicion():
  print("La criatura que aparece es:", aparecer_criatura())
  print("La dirección por donde apareció la criatura es:", aparecer_direccion())

def grito_marinero(criaturas, direccion):

  articulo_criatura = None
  articulo_direccion = None

  if criaturas == "Kraken" or criaturas == "Hipocampo" or criaturas == "Pulpo":
    articulo_criatura = "un"
  if criaturas == "Sirenas" or criaturas == "Hidras":
    articulo_criatura = "unas"
  if criaturas == "Ballena" or criaturas == "Macaraprono":
    articulo_criatura = "una"
  if criaturas == "Leviatanes":
    articulo_criatura = "unos"

  if direccion == "babor" or direccion == "estribor":
    articulo_direccion = "a"
  if direccion == "proa" or direccion == "popa":
    articulo_direccion = "por la"

  return articulo_criatura, articulo_direccion

def imprime_grito(articulo_criatura, criaturas, articulo_direccion, direccion):
  print("Ahoy! capitán, " + articulo_criatura+" " + criaturas+" " + articulo_direccion+" " + direccion)

def header_main(title):
  print("#"*(len(title)+7))
  print("#\t"+title+"\t#")
  print("#"*(len(title)+7))
  print("")
