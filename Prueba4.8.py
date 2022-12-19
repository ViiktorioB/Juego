#Viktorio Burchin
#Escribe un programa que pida la anchura de un triángulo y lo dibuje de la siguiente manera:
#Altura del triángulo: 4
#*
#**
#***
#****
#***
#**
#*
# Inicio
# En este ejercicio se hace una mezcla de los dos anteriores
NumeroAnch= int(input("Introduce la anchura del triangulo para realizar la operacion: "))
for i in range(NumeroAnch+1):
  for j in range(i):
      print("* ", end="")
  print()
for i in range(1,NumeroAnch): # al añandir el 1 delante del rango hacemos que nos elimine el duplicado que nos crea porque empezara en el segundo valor [1]
  for j in range(NumeroAnch - i): 
     print("* ", end="")
  print()