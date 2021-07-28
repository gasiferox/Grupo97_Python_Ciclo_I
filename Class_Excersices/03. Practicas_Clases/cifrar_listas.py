cifrado=str(input("Ingrese por favor el texto a cifrar: "))

p_clave="murcielago"
p_tradu="0123456789"

lista_clave=list(p_clave)
lista_tradu=list(p_tradu)

for i in range(len(p_clave)):
  cifrado=cifrado.replace(lista_clave[i], lista_tradu[i])

tempcifrado = cifrado
print(cifrado)

for i in range(len(p_clave)):
  tempcifrado=tempcifrado.replace(lista_tradu[i], lista_clave[i])

print(tempcifrado)
