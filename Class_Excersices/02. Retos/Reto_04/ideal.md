#Método IDEAL

## Identificar
* Cual es el problema?
  
  Se quiere implementar una contraseña segura con ciertos parámetros de verificación.

* Cuales son los interesados?

  Programa de la Misión TIC.

* Cual es el objetivo?

  Generar una clave de 23 caracteres que contenga las 2 ininiales u
  de una region y una clave de verificación proveniente de la misma clave generada.

* Existen restricciones?

  * La clave debe tener 23 caracteres alfanuméricos.
  * La clave debe contener la dos iniciales de cada región en los índices 9 y 11.
  * Los tres ultimos caracteres deben estar contenidos en las posiciones de los indices 3, 4 y 7 de la clave.

## Definir

  * Que conozco?

    * Región
    * Números
    * Letras

  * Que debo conocer?

    * La nueva clave

  * Dividir el problema en subproblemas

    * Dado un conjunto de números, letras y nombres de regiones, convertirlos todos a listas.
    * Generar una lista con la suma de los números y letras.
    * Generar una lista con caracteres aleatorios provenientes de la lista anterior.
    * Generar una lista con las iniciales de las regiones.
    * Realizar la comparación según sea la región para crear lista con las dos primeras letras de cada palabra.
    * Realizar la unión de las listas, en la clave final.

## Estrategia

  * Hacer ejemplos particulares para entender el problema y sus subproblemas.

    * region: "PUTUMAYO"
      La clave es: __TCY3V5YT8PRUXTC5TN0D35T__

  * Identificar opciones y estrategias de solución general.

    * Recibir la palabra región.

    * Armar varias listas con cada una de las palabras a utilizar.

    * Generar la clave a partir del uso de las listas siguiendo los parámetros de las restricciones, mediante la asignación de índices de lista.

## Algoritmo

  * Especificar requisitos para cada subproblemas.
  * Escribir algoritmos para cada requisito.
  * Escribir el algoritmo general.
  * Realizar pruebas de escritorio.

## Logro --> Programa

  * Programar los algoritmos en Python.
  * Probar el programa.
