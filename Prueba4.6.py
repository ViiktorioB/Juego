# Viktorio Burchin
# Escribe un programa que pida la altura de un triángulo y lo dibuje de la siguiente manera:
#*
#**
#***
#****
# Inicio
NumeroAlt = int(input("Introduce la altura del triangulo para realizar la operacion: "))
# En este caso usamos + 1 porque necesitamos que el valor de una esquina empieze por *
for i in range(NumeroAlt+1):
  for j in range(i):
      print("* ", end="")
  print()
