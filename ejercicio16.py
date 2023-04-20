##Crea dos listas con la misma cantidad de elementos y luego crea una tercera lista que contenga los elementos de ambas listas intercalados. 
##Por ejemplo, si las dos listas son [1, 2, 3] y ["a", "b", "c"], la tercera lista debería ser [1, "a", 2, "b", 3, "c"].

lista1 = [1, 2, 3]
lista2 = ["a", "b", "c"]

resultado = [elem for tupla in zip(lista1, lista2) for elem in tupla]
print(resultado)