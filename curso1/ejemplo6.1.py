#!/usr/bin/env python

__author__ = "Alberto Valero"
__copyright__ = "Copyright 2016, BeJob Santillana"
__credits__ = ["Victor Gonzalez"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Alberto Valero"
__email__ = "alberto.valero@bq.com"
__status__ = "Production"


l = list()	                       #Creamos una lista vacia
texto = input("Introduce un número entero por teclado: ")
if texto.isnumeric():               # Comprobamos si son numeros
	num = int(texto)
	l.append(num)
	print("Número " + str(num) + " añadido a la lista")
else:
	print("No has introducido un número entero")
