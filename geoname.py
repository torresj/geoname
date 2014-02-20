from lxml import etree

#Abrimos el archivo de las ciudades
infile = open('ciudades.txt', 'r')

#Hacemos un while con lectura anticipada para leer cada ciudad
linea=infile.readline()

while linea!="":
	#Contstruimos la direccion http para realizar la consulta con la ciudad leida
	http="http://api.geonames.org/search?username=torresj&name="+linea
	#Convertimos en un "arbol" el archivo xml
	tree = etree.parse(http)

	geoname = tree.getroot() # elemento raiz
	
	# Primer hijo, que coincide con el objeto geoname con la ciudad y sus datos
	ciudad = geoname[1] 
	
	#Varibale para imprimir
	cadena=""
	#Recorremos los atributos de la ciudad y usamos solo el nombre y la geoposicion
	for e in ciudad:
		if (e.tag == 'name'):
			cadena=cadena+e.text+" "
		if (e.tag == 'lat'):
			cadena=cadena+e.text+" "
		if (e.tag == 'lng'):
			cadena=cadena+e.text+" "
			print (cadena)

	#Leemos la siguiente ciudad
	linea=infile.readline()


#Cerramos el archivo de las ciudades
infile.close()

    




