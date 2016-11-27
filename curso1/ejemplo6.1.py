l = list()	                       #Creamos una lista vacia
texto = input("Introduce un número entero por teclado: ")
if texto.isnumeric():               # Comprobamos si son numeros
	num = int(texto)
	l.append(num)
	print("Número " + str(num) + " añadido a la lista")
else:
	print("No has introducido un número entero")
