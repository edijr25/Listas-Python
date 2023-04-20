##Crea una lista con los nombres de tus 3 deportes favoritos y luego agrega otro deporte al final de la lista.

lista_deportes = []

for deporte in  range (3):
    deporte = input("Ingrese su deporte favorito:")
    lista_deportes.append (deporte)
    

print ("Lista sin editar:")
print (lista_deportes)
print ("----------")

lista_deportes.append ("Golf")
print (lista_deportes)