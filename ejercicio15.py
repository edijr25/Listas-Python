##Crea una lista de números enteros y luego encuentra la suma de los números en índices impares.

lista1 = [2, 4, 6, 8, 10, 12, 13, 17, 18, 20]
impares= 0
for numeros in lista1:
    if numeros % 2 !=0:
        impares += numeros

print(impares)