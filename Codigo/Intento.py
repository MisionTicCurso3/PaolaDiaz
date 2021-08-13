#Escribir un programa para comprar un helado.
#Identificar cuanto se le quiere agregar.
print("Que helado y topping quieres comprar")
h1 = 1.900
t1 = float (str(1.000 + h1))
t2 = float (str(1.500 + h1))
t3 = float (str(2.500 + h1))
t4 = float (str(950 + h1))
helado1 = (input("El helado sin topping: ")) 
if helado1 == "si" :
    print("El costo del helado es: ", h1)
else:
    print("Observe los siguientes topping")
topping1 = (input("El topping de oreo: "))
if topping1 == "si" :
    print("El costo de la topping de oreo es: ", t1)
else:
    print("observe el siguiente topping")
topping2 = (input("El topping de kitkat: "))
if topping2 == "si" :
    print("El costo del topping es: ", t2)
else:
    print("observe el siguiente topping")
topping3 = (input("El topping de brownie: ")) 
if topping3 == "si" :
    print("El costo del topping es: ", t3)
else:
    print("observe el siguiente topping")
topping4 = (input("El topping de barquillo: "))
if topping4 == "si" :
    print("El costo del topping es: ", t4)
else:
    print("ya se acabaron los topping")
usuario = (input("Encontro el topping deseado?: "))
if usuario == "si":
    print("Gracias por su compra")
else:
    print("No tenemos este topping, lo sentimos.")
    print("Si desea este es el precio del helado sin topping", h1)

