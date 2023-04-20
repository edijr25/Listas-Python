##Crea dos listas de 10 números enteros cada una y realiza una multiplicación de los elementos con el mismo índice en ambas listas.

lista1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
lista2 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

resultado = []

for i in range (len(lista1)):
    resultado.append (lista1[i]* lista1[i])

print(lista1)
print ("************")
print (lista2)
print ("----------------")
print (resultado)