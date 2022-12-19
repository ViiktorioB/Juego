# Iniciamos 
# Escribe un programa que pida un número y calcule su factorial.

from imaplib import Int2AP
from math import factorial

# Pides el numero que quiers callcular
Numero1 = int(input("Introduzca el numero que quieres factorial :"))

# Hace un rango del numero que te han daod y calculas su factorial
for i in range(Numero1):
    fact = factorial(Numero1)
print("El factorial de",Numero1, "es :", fact)

