""" Programa calculadora artimética super amigable#
    Realiza las 4 operaciones (+,-,* /)
    dada como entrada una cadena de caracteres
    incorpora al modulo calculadora_aritmetica.py

    Gustavo Romero Nocua
    gasifero@gmail.com
    
    Junio 12-2021 """

#---------------- Zona librerias------------
import calculadora_aritmetica as calc
import functions as f
from tabulate import tabulate

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------

##Se llevó esta función al documento de funciones (calculadora_aritmetica.py) de la carpeta

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

header=f.header_main()
header

ascii_pic=f.ascii_pic()
ascii_pic

#TODO: Leer cadena de entrada
#num_1,num_2,op= parser_cadena(cadena_entrada)

cadena_entrada=input("Ingrese la operacion bajo el siguiente formato \n[numero_entero operador numero_entero]: ")

#TODO: terminar programa

numero_uno,numero_dos,operando = f.parser_cadena(cadena_entrada)

suma=calc.sumar_numeros(numero_uno, numero_dos)
resta=calc.restar_numeros(numero_uno, numero_dos)
multiplicacion=calc.multiplicar_numeros(numero_uno, numero_dos)
division=calc.dividir_numeros(numero_uno, numero_dos)

resultado=None

if operando == "+":
  resultado=suma
elif operando == "-":
  resultado=resta
elif operando == "*":
  resultado=multiplicacion
elif operando == "/":
  resultado=division
else:
  print("El operador no es correcto, revise el formato de ingreso")

print("\nEl resultado obtenido por esta operación es: ",resultado)
print("\nLos componentes de la operación son los siguientes: \n")

tabla=[["Número_uno:", numero_uno],["Número_dos:", numero_dos],["Operando:", operando],["Resultado",resultado]]

print(tabulate(tabla,headers=["Componente","Asignación"],tablefmt="fancy_grid"))
