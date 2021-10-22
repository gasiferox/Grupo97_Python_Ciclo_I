def busqueda_binaria(letra:str)->int:
    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encontrado = False
    inicio = 0
    indice = 0
    final = len(alfabeto)-1
    while not encontrado:
        mitad = (final + inicio) // 2
        if mitad < 0:
            encontrado = True
            """ indice = -1 """
        elif alfabeto[mitad] == letra:
            encontrado = True
            indice += 1
        elif alfabeto[mitad] < letra:
            inicio = mitad + 1
            indice += 1
        else:
            final = mitad - 1
    return indice

busqueda_binaria("Z")
indice = busqueda_binaria("Z")
print(indice)

def operar_en_lista(lista):
    n = len(lista)
    i = 0
    while i < n:
        j = 0
        while j < (n - i -1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            j += 1
        i += 1
    return lista

lista = operar_en_lista([5,10,7])
print(lista)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibo = fibonacci(14)
print(fibo)

def palindromo(frase):
    frase = frase.replace(" ","")
    if len(frase) <= 1:
        return True
    elif frase[0] == frase[-1]:
        return palindromo(frase[1:-1])
    else:
        return False

frase = "anita lava la tina"
palin = palindromo(frase)
print(palin)

def funcion(numero_1, numero_2):
    i = 1
    encontrado = False
    producto = max(numero_1, numero_2)
    while not encontrado:
        if producto % numero_1 == 0 and producto % numero_2 == 0:
            encontrado = True
        else:
            i += 1
            producto = max(numero_1, numero_2) * i
    return producto

f = funcion(3, 6)
print(f)

def invertir_palabra(palabra):
    respuesta = ""
    i = 0
    while i < len(palabra):
        respuesta += palabra[len(palabra) - 1 - i]
        leni= (len(palabra)-1-i)
        i += 1
    return respuesta

inv = invertir_palabra("hola")
print(inv)

def operar_en_lista(lista):
    menores = []
    mayores = []
    centrales = []
    if len(lista) <= 1:
        return lista
    else:
        central = lista[0]
        i = 0
        while i < len(lista):
            if lista[i] < central:
                menores.append(lista[i])
            elif lista[i] > central:
                mayores.append(lista[i])
            else:
                centrales.append(lista[i])
            i += 1
        menores = operar_en_lista(menores)
        mayores = operar_en_lista(mayores)
    return menores + centrales + mayores

lista = ["X", "Z", "W"]
print(operar_en_lista(lista))

def funcion(img):
    for i in range(0, len(img)):
        for j in range(0, len(img[i]) // 2):
            pix = img[i][j]
            img[i][j] = img[i][len(img[i])-1-j]
            img[i][len(img[i])-1-j] = pix
    return img

image = [[1,0],[0,-1]]
print(funcion(image))