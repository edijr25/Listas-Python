##Crea una lista vacía y pide al usuario que ingrese una palabra. Luego, muestra la primera letra de la palabra. 
##Repite este proceso hasta que el usuario ingrese una palabra que comience con la letra "z".


lista_nombres = []

while True:
    nombre = input("Ingrese un nombre: ")
    lista_nombres.append (nombre)
    if nombre.startswith('z'):
        break
print ("La primera letra de los nombres es: ", nombre[0])
print("La lista de nombres es: ",lista_nombres)
