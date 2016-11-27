#!/usr/bin/env python

__author__ = "Alberto Valero"
__copyright__ = "Copyright 2016, BeJob Santillana"
__credits__ = ["Victor Gonzalez"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Alberto Valero"
__email__ = "alberto.valero@bq.com"
__status__ = "Production"

import pickle
from pathlib import Path

#Create an empty dictionary
d = dict()

#Ask for file name to load dictionary from
file_name = input("Introduce el nombre del archivo con los datos: ")

#Comprobamos que existe
path = Path(file_name)
if path.is_file():
	# Open file in reading mode
	input_file = open(file_name, 'rb')
	d = pickle.load(input_file)
	#Close de file
	input_file.close()
else:
	print("El file no existe, creamos diccionario vacio")


#Check for values or add new ones
document_number = input("Introduce un documento de indentidad ")

if document_number in d: 	#Check whether it is on dict or not
	print("La edad de " + document_number + " es " + str(d[document_number]))
else:
	age = input("Documento no existente. Introduce edad: ") 
	if age.isnumeric():
		num = int(age)
		d[document_number] = num
		print("Añadido al diccionario")

# Save dict on file and close
output_file = open(file_name, 'wb')
pickle.dump(d, output_file)
output_file.close()
