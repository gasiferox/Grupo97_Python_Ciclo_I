
def obtener_prioritarios(lista_pacientes):
    lista_prioritarios=[]
    for paciente in lista_pacientes:
        if paciente["edad"]>=50:
            lista_prioritarios.append(paciente)
    return lista_prioritarios


lista_personas=[]

persona1={
    "nombre":"luis",
    "cedula":123,
    "edad":80
}

lista_personas.append(persona1)

persona2={
    "nombre":"Maria",
    "cedula":456,
    "edad":30
}

lista_personas.append(persona2)

persona3={
    "nombre":"Tomás",
    "cedula":789,
    "edad":67
}

lista_personas.append(persona3)

lista_prioritarios = obtener_prioritarios(lista_personas)

print("La lista de los prioritarios es ",lista_prioritarios)

#print(lista_personas)
