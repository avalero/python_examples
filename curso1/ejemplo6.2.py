#!/usr/bin/env python

__author__ = "Alberto Valero"
__copyright__ = "Copyright 2016, BeJob Santillana"
__credits__ = ["Victor Gonzalez"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Alberto Valero"
__email__ = "alberto.valero@bq.com"
__status__ = "Production"


d = { "50862634" : 37 , "43394932" : 32} 	#Creamos diccionario 

texto = input("Introduce un documento de indentidad ")


if texto in d: 	#Comprobamos si esta en el diccionario
	print("La edad de " + texto + " es " + str(d[texto]))
else:
	edad = input("Documento no existente. Introduce edad: ") 
	if edad.isnumeric():
		num = int(edad)
		d[texto] = num
		print("Añadido al diccionario")
	
print(d)   #Mostramos por pantalla el diccionario
