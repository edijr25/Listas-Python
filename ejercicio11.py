##Crea una lista de palabras y pide al usuario que ingrese una palabra. 
##Luego, muestra todas las palabras de la lista que tienen la misma longitud que la palabra ingresada.

lista_palabras = ["hola", "mundo", "python", "programación", "lista"]
palabra = input("Ingrese una palabra: ")
lista_palabras.append (palabra)

for palabras in lista_palabras:
    if (len(palabras) == (len(palabra))):
        print(palabras)