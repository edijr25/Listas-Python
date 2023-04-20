##Solicitar al usuario números enteros hasta que ingrese el 0. 
##Almacenar los números en una lista y luego imprimir el mayor

lista_numero = []

while True:
    numero = int(input("Ingrese un numero (coloque el 0 para terminar): "))
    if numero == 0:
        break
    lista_numero.append (numero)

if len(lista_numero) == 0 :
    print("No se ingresaron numeros")
else:
    mayor = lista_numero[0]
    for i in range(1, len(lista_numero)):
        if lista_numero[i] > mayor:
            mayor = lista_numero[i]
    print("El número mayor es:", mayor)
