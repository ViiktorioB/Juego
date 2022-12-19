# Viktorio B
# Escribe un programa que pida un número e imprima todos sus divisores.
Numero = int(input("Introduce el numero que quieras comprobar: "))
#Creamos el rango mas uno para que no nos quente el 0 ya que nos daria error y al selecinar 1 al principo del rango hace que contemos el ultimo numero como divisor
for i in range(1,Numero+1):
     if Numero % i == 0:
        print(i, "ES DIVISOR")

