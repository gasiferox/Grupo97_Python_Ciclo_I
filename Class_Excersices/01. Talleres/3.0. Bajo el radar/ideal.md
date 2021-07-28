# Identificar
* Cual es el problema?
  
  Se quiere evitar la accidentalidad vehicular por alta velocidad y alcoholemia.

* Cuales son los interesados?

  Secretaría de tránsito.

* Cual es el objetivo?

  Generar multas por velocidad y alcoholemia.

* Existen restricciones?

  * El rango del grado de alcoholemia esta entre 20 a 150 mg / 100 ml

# Definir

  * Que conozco?

    * Distancia 1
    * Distancia 2
    * Tiempo entre distancias
    * La formula
    
      `velocidad = distancia / tiempo`

  * Que debo conocer?

    * Velocidad
    * Multa por velocidad
    * Multa por alcoholemia

  * Dividir el problema en subproblemas

    * Funcion que calcule la velocidad y determine si merece o no una multa.
    * Función que calcule la clasifición rango de alcoholemia y detemine si requiere o no una multa.

# Estrategia

  * Hacer ejemplos particulares para entender el problema y sus subproblemas.

    * Si un vehículo esta a 500 m y luego a 100 m en 20 s el resultado es 20 m/s igual a 72 km/h y recibiria un llamado de atención por alta velocidad.

    * Si un vehículo esta a 500 m y luego a 100 m en 40 s el resultado es 10 m/s igual a 36 km/h y devuelve un mensaje con velocidad normal.

    * Si un vehículo esta a 500 m y luego a 100 m en 10 s el resultado es 40 m/s igual a 144 km/h y recibiria una multa tipo II e inmovilización del vehículo.

  * Identificar opciones y estrategias de solución general.

    * Realizar el cálculo de la velocidad del vehículo.

    * Determinar si merece multa por velocidad o por alcoholemia.

    
# Algoritmo

  * Especificar requisitos para cada subproblemas.
  * Escribir algoritmos para cada requisito.
  * Escribir el algoritmo general.
  * Realizar pruebas de escritorio.

# Logro --> Programa

  * Programar los algoritmos en Python.
  * Probar el programa.
