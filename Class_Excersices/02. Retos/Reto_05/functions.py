""" RETO 5
    FUNCIONES PARA TRABAJAR CON DICCIONARIOS Y LISTAS

    Gustavo Romero Nocua
    gasifero@gmail.com
    
    Junio 24-2021
    """

def contar_cantidad_cursos(lista_cursos)->int:
    cantidad_cursos = 0
    for curso in lista_cursos:
        if curso["nombre"] == "FP":
            cantidad_cursos += 1

    return cantidad_cursos

def contar_cantidad_cursos_buscado(lista_cursos, curso_buscado)->int:
    cantidad_cursos = 0
    for curso in lista_cursos:
        if curso["nombre"] == curso_buscado:
            cantidad_cursos += 1

    return cantidad_cursos

def contar_cantidad_cursos_profesor(lista_cursos, cedula_profesor)->int:
    cantidad_cursos = 0
    for curso in lista_cursos:
        profe_curso = curso["profesor"]
        if profe_curso["cedula"] == cedula_profesor:
            cantidad_cursos +=1

    return cantidad_cursos

def calcular_matriculados(lista_cursos)->int:
    total_matriculados = 0
    for curso in lista_cursos:
        if curso["nombre"] == "FP":
            total_matriculados += len(curso["estudiantes"])

    return total_matriculados

def calcular_notas_finales(lista_cursos):
    for curso in lista_cursos:
        for estudiante in curso["estudiantes"]:
            lista_notas = estudiante["notas"]
            estudiante["nota_final"]=lista_notas[0]*0.3+lista_notas[1]*0.35+lista_notas[2]*0.35
            print("El estudiante,",estudiante["nombre"], "del curso de", curso["nombre"], "obtuvo una nota final de", estudiante["nota_final"])

def calcular_estadisticas(lista_cursos)->int:
    cantidad_ganadores = 0
    cantidad_recuperaciones = 0
    cantidad_perdidas = 0

    for curso in lista_cursos:
        if curso["nombre"] == "FP":
            for estudiante in curso["estudiantes"]:
                lista_notas = estudiante["notas"]
                estudiante["nota_final"] = lista_notas[0]*0.3 + lista_notas[1]*0.35 + lista_notas[2]*0.35
                if estudiante["nota_final"] >= 3.0:
                    cantidad_ganadores += 1
                elif estudiante["nota_final"] < 3.0 and estudiante["nota_final"] >= 2.2:
                    cantidad_recuperaciones += 1
                elif estudiante["nota_final"] < 2.2:
                    cantidad_perdidas += 1

    return cantidad_ganadores, cantidad_recuperaciones, cantidad_perdidas
