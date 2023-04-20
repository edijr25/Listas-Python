##Crear un programa que solicite al usuario ingresar precio unitario y cantidad de 5 productos. 
##Almacenar cada valor en dos listas distintas. Luego imprimir el precio total de cada artículo.

# Creamos dos listas vacías para almacenar los precios unitarios y las cantidades
precios = []
cantidades = []

# Pedimos al usuario que ingrese el precio unitario y la cantidad de cada producto
for i in range(5):
    precio = float(input(f"Ingrese el precio unitario del producto {i+1}: "))
    cantidad = int(input(f"Ingrese la cantidad del producto {i+1}: "))
    precios.append(precio)
    cantidades.append(cantidad)

# Imprimimos el precio total de cada producto multiplicando el precio unitario por la cantidad
for i in range(5):
    precio_total = precios[i] * cantidades[i]
    print(f"El precio total del producto {i+1} es: {precio_total}")
