# Escribe un programa que pida dos números y escriba la suma de enteros desde el primero hasta el último.
# Pedimos los valores que necesitamos 
Numero1 = int(input("Introduzca el primer numero :"))
Numero2 = int(input("Introduzca el segundo numero, que sea mayor que " + str(Numero1) + ":"))
# Creamos la varible que nos muestre ne pantalla la suma de numero con le siguiente y nos incremnte otro valor con el contador su
su = 0
for i in range(Numero1,Numero2+1):
      su = su + i
# Mostramos por pantalla el resultado
print("La suma de entre los numeros", Numero1, "y", Numero2,"es de", su)
