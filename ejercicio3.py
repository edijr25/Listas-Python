##Crea una lista vacía y pide al usuario que ingrese números enteros hasta que ingrese un número negativo. 
##Luego, muestra la suma de todos los números ingresados.

lista = []
suma_numeros = 0

while True:
    nuevo_numero = int(input("Ingresa un nuevo numero (Ingresa un numero negativo al acabar): "))
    suma_numeros += nuevo_numero
    if nuevo_numero < 0:
        break

    lista.append(nuevo_numero)

print("La suma de los numeros ingresados es ",suma_numeros)