# Viktorio Burchin
#
NumeroAlt= int(input("Introduce la altura del cuadrado para realizar la operacion: "))
NumeroAnch= int(input("Introduce la anchura del cuadrado para realizar la operacion: "))
for i in range(1,NumeroAlt+1):
    if i % 2 == 0:
        print("*", end=" ")
    else:
        print(" ", end=" ")
print()