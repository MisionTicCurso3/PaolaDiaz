#Escribir un programa para comprar un helado.
#Identificar cuanto se le quiere agregar.
print("Que helado y topping quieres comprar")
Valor_final = 0
h1 = 1900
t1 = 1000 
t2 = 1500 
t3 = 2500 
t4 = 950 
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
def Valor_final(helado, topping):
    Valor_final = 0
    Valor_final = h1 + topping
    if (helado1-topping4) == "si":
        print("El costo total del helado es: ", Valor_final)
    else:
        print("comentarios del usuario")
Valor_final(h1,input())
usuario = (input("Encontro el topping deseado?: "))
if usuario == "si":
    print("Gracias por su compra")
else:
    print("No tenemos este topping, lo sentimos.")
    print("Si desea este es el precio del helado sin topping", h1)

