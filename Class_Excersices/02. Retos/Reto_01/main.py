'''
Gustavo Romero Nocua
gasifero@gmail.com

### RETO NO.1 - FUNDAMENTOS DE PROGRAMACIÓN - CICLO I - GRUPO 97 ###

'''

#importamos las funciones del archivo y lo llamamos f
import functions as f

#solicitamos las variables de trabajo
nota_final = float(input("Introduzca la nota final del estudiante: "))

mensaje = f.determinar_notificacion(nota_final)
letra_nota = f.conversion_sistema_americano(nota_final)

print("\nSegún la nota obtenida por el estudiante, el mismo",mensaje,"la materia.\n\nLa nota equivalente en el sistema americano es: ",letra_nota)
