#Crear un programa que pida dos numeros enteros al usuario y diga si alguno de ellos es multiplo del otro.
# Crea una funcion es multiplo que reciba los 2 numeros y muestre un mensaje si es multiplo o no.
print("Dijita dos numero enteros.")
num1 = int (input("Escribe un numero entero: "))
num2 = int (input("Escribe otro numero entero"))
print("El primer numero entero es: " + str(num1) + " El segundo numero entero es: " + str(num2))
multiplo = 0 
multiplo = num1 % num2
if multiplo == 0 :
    print("Es un multiplo")
else:
    print("No es un multiplo")

