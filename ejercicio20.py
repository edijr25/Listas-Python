##A partir de la lista: [1,80,5,0,15,-5,1,79] determinar:
## el mayor, el menor, el promedio y la suma total de todos los elementos

lista = [1,80,5,0,15,-5,1,79] 
menor= 0
mayor = 0
suma = 0

for numero in lista:
    suma += numero 
    if mayor < numero:
        mayor = numero
    
    if menor > numero:
        menor = numero
promedio = suma / len(lista)

print("El numero mayor es ",mayor)
print ("El numero menor es", menor)
print ("La suma de toda la lista es",suma)
print ("El promedio es ", promedio)