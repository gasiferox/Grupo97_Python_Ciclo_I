#9.5. Ejercicios
Algoritmos de Programación con Python

https://uniwebsidad.com/libros/algoritmos-python/capitulo-9/ejercicios-12

**Ejercicio 9.5.1.** Escribir una función que reciba una lista de tuplas, y que devuelva un diccionario en donde las claves sean los primeros elementos de las tuplas, y los valores una lista con los segundos.

Por ejemplo:

`l = [ ('Nola', 'don Pepito'), ('Nola', 'don Jose'), ('Buenos', 'días') ]
print tuplas_a_diccionario(l)`

`Deberá mostrar: { 'Nola': ['don Pepito', 'don Jose'], 'Buenos': ['días'] }`

__Ejercicio 9.5.2. Diccionarios usados para contar.__

1. Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1
2. Escribir una función que cuente la cantidad de apariciones de cada carácter en una cadena de texto, y los devuelva en un diccionario.
3. Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos dados. Nota: utilizar el módulo random para obtener tiradas aleatorias.

__Ejercicio 9.5.3. Continuación de la agenda.__

Escribir un programa que vaya solicitando al usuario que ingrese nombres.

1. Si el nombre se encuentra en la agenda _(implementada con un diccionario)_, debe mostrar el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
2. Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente. El usuario puede utilizar la cadena "*", para salir del programa.

__Ejercicio 9.5.4.__ Escribir una función que reciba un texto y para cada caracter presente en el texto devuelva la cadena más larga en la que se encuentra ese caracter.
