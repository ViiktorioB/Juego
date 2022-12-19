# Viktorio Burchin
#
NumeroAlt = int(input("Introduce la altura del triangulo para realizar la operacion: "))
for i in range(NumeroAlt+1):
  for j in range(NumeroAlt - i):
      print(" ", end="")
  for j in range(1,2*i):
      print("*", end="")
  print()

