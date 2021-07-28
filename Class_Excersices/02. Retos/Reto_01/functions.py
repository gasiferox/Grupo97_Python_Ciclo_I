'''
Funciones para el reto_1


'''

### RT_1_A
def determinar_notificacion(nota_final)->str:

  if nota_final >= 0 and nota_final <= 5:

    mensaje=""

    if nota_final >= 3 and nota_final <= 5:
      mensaje="gana"
    elif nota_final >= 2.2 and nota_final < 3:
      mensaje="recupera"
    else:
      mensaje="pierde"

    return mensaje

  else:
    print("La nota ingresada no es válida por favor ingrese de nuevo el valor correcto!")

    mensaje="error"

    return mensaje


### RT_1_B
def conversion_sistema_americano(nota_final)->str:

  grado_numerico = nota_final * 100 / 5

  if nota_final >= 0 and nota_final <= 5:

    letra_nota=""

    if grado_numerico >= 90 and grado_numerico <= 100:
      letra_nota="A"
    elif grado_numerico >= 80 and grado_numerico < 90:
      letra_nota="B"
    elif grado_numerico >= 70 and grado_numerico < 80:
      letra_nota="C"
    elif grado_numerico >= 69 and grado_numerico < 70:
      letra_nota="D"
    else:
      letra_nota="F"

    return letra_nota

  else:

    print("La nota ingresada no es válida por favor ingrese de nuevo el valor correcto!")

    mensaje="error"

    return mensaje
