##Crear un programa que solicite al usuario ingresar: nombre del producto, cantidad y precio unitario. 
##Guardar los datos en 3 listas distintas. 
##Solicitar productos hasta que el nombre del producto sea ‘xxx’. 
##Luego imprimir la lista de artículos con el siguiente formato:
##nombre_articulo	cantidad	$ precio_unitario 	$ total
##	Ejemplo:
##	alfajor capitan del espacio		6	$ 150		$ 900

nombres = []
cantidades = []
precios_unitarios = []


while True:
    nombre= (input(f"Ingrese nombre del producto: "))
    if nombre == 'xxx':
        break
    precio = float(input(f"Ingrese el precio unitario del producto: "))
    cantidad = int(input(f"Ingrese la cantidad del producto: "))
    nombres.append (nombre)
    precios_unitarios.append(precio)
    cantidades.append(cantidad)

print("Nombre del articulo\tCantidad\t$ Precio unitario\t$ Total")
for i in range(len(nombres)):
    total = cantidades[i] * precios_unitarios[i]
    print(f"{nombres[i]}\t    \t{cantidades[i]}     \t$ {precios_unitarios[i]}\t       \t$ {total}")

