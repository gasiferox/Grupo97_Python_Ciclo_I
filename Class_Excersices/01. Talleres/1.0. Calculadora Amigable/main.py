""" Programa calculadora artimética amigable#
    Realiza las 4 operaciones (+,-,* /)
    incorpora al modulo calculadora_aritmetica.py
    Gustavo Romero Nocua
    gasifero@gmail.com
    Junio 12-2021 """

#---------------- Zona librerias------------
import calculadora_aritmetica as calc

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

def menu_operaciones():
  print("==================================================")
  print("| Menu                                           |")
  print("==================================================")
  print("| Ingresa un numero para realizar la operacion.  |")
  print("==================================================")
  print("| 1. Calcular suma: (1)                          |")
  print("==================================================")
  print("| 2. Calcular la resta: (2)                      |")
  print("==================================================")
  print("| 3. Calcular multiplicación: (3)                |")
  print("==================================================")
  print("| 4. Calcular división: (4)                      |")
  print("==================================================")

  opcion = int(input("\nIngrese la opción de su preferencia: "))
  return opcion

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
opcion=int(menu_operaciones())

numero_uno = float(input("Por favor ingrese el primer número: "))
numero_dos = float(input("Por favor ingrese el segundo número: "))

suma = calc.sumar_numeros(numero_uno, numero_dos)
resta = calc.restar_numeros(numero_uno,numero_dos)
multiplicacion = calc.multiplicar_numeros(numero_uno,numero_dos)
division = calc.dividir_numeros(numero_uno,numero_dos)

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

if opcion >= 1 and opcion <= 4:

  if opcion == 1:
    print("El resultado de la suma de los dos números es: ",suma)
  elif opcion == 2:
    print("El resultado de la resta de los dos números es:",resta)
  elif opcion == 3:
    print("El resultado de la multiplicación de los dos números es:",multiplicacion)
  elif opcion == 4:
    print("El resultado de la división de los dos números es:",division)

else:
  print("### La opción ingresada no es válida ###")
