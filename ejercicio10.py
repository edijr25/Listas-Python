""" ##Crea una lista de palabras y muestra las palabras que tienen más de 5 letras.

# Pedimos al usuario que ingrese una lista de palabras separadas por comas
lista_palabras = input("Ingrese una lista de palabras separadas por comas: ")

# Convertimos la entrada del usuario en una lista de palabras
palabras = lista_palabras.split(',')

# Iteramos por cada palabra en la lista
for palabra in palabras:
    # Si la longitud de la palabra es mayor que 5, la imprimimos
    if len(palabra.strip()) > 5:
        print(palabra.strip())
 """

# Creamos una lista de palabras
palabras = ['Python', 'programación', 'ordenador', 'teclado', 'mouse', 'pantalla']

# Iteramos por cada palabra en la lista
for palabra in palabras:
    # Si la longitud de la palabra es mayor que 5, la imprimimos
    if len(palabra) > 5:
        print(palabra)
