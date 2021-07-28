import random as r


IMAGENES_AHORCADO = ['''

  +---+
  |   |
      |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
      |
=========''']

palabras = "hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro" \
           " burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula " \
           "salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon " \
           "oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo " \
           "wombat cebra".split()


def obtenerPalabraAlAzar(palabras):
    indicePalabras = r.randint(0, len(palabras) - 1)

    return palabras[indicePalabras]
#    palabraAlAzar = r.choice(palabras)
#    indicePalabra = r.randint(0, len(palabraAlAzar)-1)

#    return palabraAlAzar[indicePalabra]

def mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta):
    print(IMAGENES_AHORCADO[len(letrasIncorrectas)])
    print()

    print("Letras incorrectas:", end=" ")
    for letra in letrasIncorrectas:
        print(letra, end=" ")
    print()
    
    espaciosVacios = "_" * len(palabraSecreta)

    # Completar los espacios vacíos con las letras adivinadas
    for i in range(len(palabraSecreta)):
        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacios = espaciosVacios[:i] + palabraSecreta[i] + espaciosVacios[i+1:]


    # Mostrar la palabra secreta con los espacios entre cada letra
    for letra in espaciosVacios:
        print(letra, end=" ")
    print()

def obtenerIntento(letrasProbadas):
    # Devuelve la letra ingresada por el jugador, verifica que el jugador ha ingresado solo una letra, y no otra cosa.
    while True:
        intento = str(input("Adivina una letra: "))
        intento = intento.lower()
        if len(intento) != 1:
            intento = str(input("Por favor introduzca una letra: "))
        else:
            return intento

def jugarDeNuevo():
    # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve false.
    print("Quiere volver a jugar de nuevo? (si ó no)")
    return input().lower().startswith("s")

print("A H O R C A D O")
letrasIncorrectas = ""
letrasCorrectas = ""
palabraSecreta = obtenerPalabraAlAzar(palabras)
juegoTerminado = False

while True:
    mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)

    # Permite al jugador escribir una letra
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

    if intento in palabraSecreta:
        letrasCorrectas = letrasIncorrectas + intento

        # Verifica si el jugador ha ganado
        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] not in letrasCorrectas:
                encontradoTodasLasLetras = False
                break
            if encontradoTodasLasLetras:
                print("¡Si! ¡La palabra secreta es ", palabraSecreta, ", ¡Has ganado!")
                juegoTerminado = True
    else:
        letrasIncorrectas = letrasIncorrectas + intento

        # Comprobar si el jugador ha agotado sus intentos y ha perdido.
        if len(letrasIncorrectas) == len(IMAGENES_AHORCADO) - 1:
            mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta)
            print("Te has quedado sin intentos!\nDespués de", str(len(letrasIncorrectas)), "intentos fallidos y ", str(len(letrasCorrectas)), "aciertos, la palabra era ", palabraSecreta, "\"")
            juegoTerminado = True

    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ""
            letrasCorrectas = ""
            juegoTerminado = False
            palabraSecreta = obtenerPalabraAlAzar(palabras)
        else:
            break
