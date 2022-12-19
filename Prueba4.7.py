#Viktorio Burchin
##Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
#Altura del triángulo: 4
#****
#***
#**
#*
# Inicio
NumeroAlt = int(input("Introduce la altura del triangulo para realizar la operacion: "))
for i in range(NumeroAlt):
  for j in range(NumeroAlt - i): # Esta linea nos permite invertir los valores ya que opera de la siguiente manera 5-0 = 5, 5-1 = 4, 5-2 =3...
      print("* ", end="")
  print()