""" Modulo funciones #
    Realiza la iteración dentro de la cadena y obtiene el operador
    y obtiene los dos numeros
    # Funciones para presentar el programa como encabezado e imagen
    Gustavo Romero Nocua
    gasifero@gmail.com
    Junio 12-2021 """

def parser_cadena(cadena_entrada)->float:
  numero_uno=""
  numero_dos=""
  operando=""

  if cadena_entrada.find("+") != -1:

    indice_op = cadena_entrada.find("+")

  elif cadena_entrada.find("-") != -1:

    indice_op = cadena_entrada.find("-")

  elif cadena_entrada.find("*") != -1:

    indice_op = cadena_entrada.find("*")

  elif cadena_entrada.find("/") != -1:

    indice_op = cadena_entrada.find("/")

  else:

    print("El operador no es correcto, revise el formato de ingreso")


  numero_uno = cadena_entrada[0:indice_op]
  numero_uno = float(numero_uno)

  numero_dos = cadena_entrada[indice_op+1:]
  numero_dos = float(numero_dos)

  operando = cadena_entrada[indice_op]


  return numero_uno, numero_dos, operando

def header_main()->str:

  print("#####################################################")
  print("#\tBienvenido a la Calculadora Super Amigable\t\t#")
  print("#####################################################\n")

def ascii_pic()->str:
  print("\t _____________________")
  print("\t|  _________________  |")
  print("\t| | GRN          0. | |")
  print("\t| |_________________| |")
  print("\t|  ___ ___ ___   ___  |")
  print("\t| | 7 | 8 | 9 | | + | |")
  print("\t| |___|___|___| |___| |")
  print("\t| | 4 | 5 | 6 | | - | |")
  print("\t| |___|___|___| |___| |")
  print("\t| | 1 | 2 | 3 | | x | |")
  print("\t| |___|___|___| |___| |")
  print("\t| | . | 0 | = | | / | |")
  print("\t| |___|___|___| |___| |")
  print("\t|_____________________|\n")

