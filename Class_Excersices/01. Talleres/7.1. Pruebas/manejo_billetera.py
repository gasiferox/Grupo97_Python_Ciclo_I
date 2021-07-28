def crear_billetera():
  billetera = {"efectivo": 0,"monedas": 0}
  return billetera

def ingresar_efectivo(billetera,efectivo):
  billetera["efectivo"]+=efectivo

def retirar_efectivo(billetera,efectivo):
  if billetera["efectivo"]==0:
    raise NameError("No tienes dinero")

  if(billetera["efectivo"] >= efectivo):
    billetera["efectivo"]-=efectivo
    return efectivo

  efectivo_restante=billetera["efectivo"]
  billetera["efectivo"]=0
  return efectivo_restante








