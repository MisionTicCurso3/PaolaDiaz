#Este es un codigo que revisara tu IMC
print("Dijite su peso en (Kg)")
Peso = float (input("Su peso en (Kg) es: "))
print("Dijite su estatura")
Estatura = float (input("su estatura en (m) es: "))
print("El resultado de su peso es:" + str(Peso) + "y su estatura es: " + str(Estatura))
print("se realizara el proceso para saber cual es su IMC")
IMC = Peso / (Estatura*Estatura)
print("su IMC es: "+ str(IMC))
if IMC <18.50 :
    print("Estas en Bajo peso")
elif IMC == 18.50:
    print("Estas en peso normal")
elif IMC == 24.99:
    print("Estas en peso normal")
else:
    print("Estas en sobrepeso")
