##rea una lista vacía y pide al usuario que ingrese una palabra. Luego,
## agrega la palabra a la lista si no se encuentra ya en la lista.
## Repite este proceso hasta que la lista tenga al menos 5 palabras.

lista_palabra = []

for palabra in range (5):
    palabra = input("Ingrese una palabra: ")
    lista_palabra.append (palabra)
    if len(lista_palabra)== 5:
        break

print (lista_palabra)
