# Viktorio Burchin
#Escribe un programa que pida la altura y ancho de un rectángulo y lo dibuje de la siguiente manera:
#Anchura del rectángulo: 5
#Altura del rectángulo: 2
#*****
#*****
# Inicio
NumeroAlt = int(input("Introduzca el anchura:"))
NumeroAnch = int(input("Introduzca el altura :"))
for i in range(NumeroAnch):
  for j in range(NumeroAlt):
    # el end se usa para que cada vez que el range vuelve en vez de realizar un salto de linea haga una concatenacion
   print("* ", end="")
  print()