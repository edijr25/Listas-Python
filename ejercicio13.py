##Crea una lista de números y encuentra el promedio de todos los números en la lista.

lista_num = [1 , 5, 6 , 7, 8, 15]
numeroTotal= 0

for numero in lista_num:
    numeroTotal += numero

promedio = numeroTotal / len(lista_num)

print ("La lista de numeros es: ")
print (lista_num)
print ("La suma de los numeros es ", numeroTotal)
print ("El promedio es ", promedio)
