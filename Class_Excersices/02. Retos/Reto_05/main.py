""" RETO 5
    PROGRAMA PARA TRABAJAR CON DICCIONARIOS Y LISTAS

    Gustavo Romero Nocua
    gasifero@gmail.com
    CC. 79942949
    Junio 24-2021
    """

import json
import functions as f

"""
Cargar el archivo
"""

with open('informacion.txt', 'r') as file:
    texto = file.read().replace("\n","")

lista_cursos = json.loads(texto)

#print(lista_grupos[0]) %% Impime el primer grupode elementos de lista grupos

################################RETO_A###############################################
print("__________________________RETO_A_________________________")
cantidad_cursos_programacion = f.contar_cantidad_cursos(lista_cursos)
print("La cantidad de cursos de programación son: ", cantidad_cursos_programacion)

################################RETO_B###############################################
print("__________________________RETO_B_________________________")
curso_buscado = "IN"
cantidad_cursos_buscados = f.contar_cantidad_cursos_buscado(lista_cursos, curso_buscado)
print("La cantidad de cursos de", curso_buscado, "es: ", cantidad_cursos_buscados)

################################RETO_C###############################################
print("__________________________RETO_C_________________________")
cedula_profesor = 123
cantidad_cursos_profesor = f.contar_cantidad_cursos_profesor(lista_cursos, cedula_profesor)
print("La cantidad de cursos que dicta el profesor con CC.", cedula_profesor, "es igual a", cantidad_cursos_profesor,"cursos.")

################################RETO_D###############################################
print("__________________________RETO_D_________________________")
cantidad_estudiantes_fp = f.calcular_matriculados(lista_cursos)
print("La cantidad de estudiantes de FP es", cantidad_estudiantes_fp)

################################RETO_E###############################################
print("__________________________RETO_E_________________________")
nota_final_estudiante = f.calcular_notas_finales(lista_cursos)

################################RETO_F###############################################
print("__________________________RETO_F_________________________")
cantidad_ganadores,cantidad_recuperaciones,cantidad_perdidas = f.calcular_estadisticas(lista_cursos)
print("Estadísticas de la materia -FP-")
print("Perdidas:",cantidad_perdidas)
print("Recuperadas:",cantidad_recuperaciones)
print("Ganadas:",cantidad_ganadores)
