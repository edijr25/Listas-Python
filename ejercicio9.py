##Crea una lista de números enteros y pide al usuario que ingrese otro número entero. 
##Luego, busca el número ingresado en la lista y muestra la posición en la que se encuentra.
## Si el número no se encuentra en la lista, muestra un mensaje indicando que no se encontró

lista_numero = [1, 2,3 ,4 ,5]

while True:
    numero = int(input("Ingrese un numero: "))
    lista_numero.append (numero)
    break

numero_buscar = int(input("Ingrese un número entero para buscar en la lista: "))

if numero_buscar in lista_numero:
    # Si el número está en la lista, imprimir su posición
    posicion = lista_numero.index(numero_buscar)
    print(f"El número {numero_buscar} se encuentra en la posición {posicion} de la lista.")
else:
    # Si el número no está en la lista, imprimir un mensaje indicando que no se encontró
    print(f"El número {numero_buscar} no se encuentra en la lista.")

print (posicion)