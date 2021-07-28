""" Modulo Multas
    Funciones para el cálculo de multas
    de tránsito
    Gustsavo Romero Nocua
    CC.79942949
    gasifero@gmail.com
    Junio 11-2021 """

# Definición de Funciones
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================
def multar_velocidad(distancia_uno, distancia_dos,tiempo):
  texto_multa=""

  velocidad = ((distancia_uno - distancia_dos)/1000) / (tiempo/3600)

  if velocidad <= 20:
    texto_multa="llamado de atención por baja velocidad"
  elif velocidad > 20 and velocidad <= 60:
    texto_multa="Normal"
  elif velocidad > 60 and velocidad <= 80:
    texto_multa="llamado de atención por alta velocidad"
  elif velocidad > 80 and velocidad <= 120:
    texto_multa="multa tipo I"
  else:
    texto_multa="multa tipo II e inmovilización del vehículo"

  return texto_multa, velocidad

def multar_alcoholemia(grado_alcohol):

  texto_multa=""

  if grado_alcohol < 20:
    texto_multa="libre de intoxicación por alcoholemia"
  elif grado_alcohol >= 20 and grado_alcohol < 40:
    texto_multa="entre 20 y 39 mg de etanol/l00 ml de sangre total, \nademás de las sanciones previstas en la presente ley, se decretará la suspensión de la licencia de conducción entre \nseis (6) y doce (12) meses"
  elif grado_alcohol >= 40 and grado_alcohol < 100:
    texto_multa="primer grado de embriaguez entre 40 y 99 mg de etanol/100 ml de sangre total, \nadicionalmente a la sanción multa, se decretará la suspensión de la Licencia de Conducción \nentre uno (1) y tres (3) años"
  elif grado_alcohol >= 100 and grado_alcohol < 150:
    texto_multa="segundo grado de embriaguez entre 100 y 149 mg de etanol/100 ml de sangre total, \nadicionalmente a la sanción multa, se decretará la suspensión de la Licencia de Conducción \nentre tres (3) y cinco (5) años, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de cuarenta (40) horas"
  else:
    texto_multa="tercer grado de embriaguez, desde 150 mg de etanol/100 ml de sangre total en adelante, \nadicionalmente a la sanción de la sanción de multa, se decretará la suspensión \nentre cinco (5) y diez (10) años de la Licencia de Conducción, y la obligación de realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente autorizados, por un mínimo de ochenta (80) horas"

  return texto_multa


