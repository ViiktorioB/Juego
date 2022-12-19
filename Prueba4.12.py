#Viktorio B
#Escribe un programa que pida un número y escriba si primo o no
Numero = int(input("Introduzca el numero que quieres comprobar:"))
# Elegimos dos despuesdel rango ya que si seleccinamos el 0 y el 1 siempe nos dira que es primo ya que tiene divisor. 
for i in range(2,Numero):
    if Numero % i != 0:
     print("El numero", Numero,"ES primo") 
     break
    # El breka lo usamos para que deje de sumar rangos ya que nos mostraria todos los divisores y no nos plantearia bien el resultado.
    else:
      print("EL numero", Numero,"NO es primo, porque es divisor de", i)
      break
