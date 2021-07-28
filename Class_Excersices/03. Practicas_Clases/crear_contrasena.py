import random

lestrasM =  ["A","B","C","D","E"]
letrasm = ["a","b","c","d","e"]
numeros = ["1","2","3","4","5"]
c_especiales = ["@","#","$","%","/"]

lista_carac = lestrasM + letrasm + numeros + c_especiales
listavacia = []

for i in range(10):
    result = random.choice(lista_carac)
    listavacia.append(result)

clave = "-".join(listavacia)

print(listavacia)
print(clave)
