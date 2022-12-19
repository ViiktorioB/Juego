# Escribe un programa que pida dos números y escriba qué números entre ese par de números son pares y cuáles impares
# Pedir dos numeros 
Numero1 = int(input("Introduzca el primer numero :"))
Numero2 = int(input("Introduzca el segundo numero, que sea mayor que " + str(Numero1) + ":"))
# Funcion que calcula el rango de los dos numeros elejidos, diciendo cuales son pares y cules impares
if Numero2 > Numero1:
  for i in range(Numero1,Numero2+1):
    if i%2 == 0:
        print(i, "ES PAR")
    else:
        print(i, "NO ES PAR")
else:
    print("El valor no es correcto")