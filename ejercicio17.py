##Crea dos listas de números y encuentra los elementos que se encuentran en ambas listas.

lista1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
lista2 = [2, 3, 6, 7, 10, 11, 14, 15, 18, 19]

lista_final = []

for numero in lista1:
    if numero in lista2:
        lista_final.append (numero)

print (lista_final)