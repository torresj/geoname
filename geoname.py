from lxml import etree

infile = open('ciudades.txt', 'r')

linea=infile.readline()

while linea!="":
	http="http://api.geonames.org/search?username=torresj&name="+linea
	tree = etree.parse(http)
	geoname = tree.getroot() # elemento raiz
	ciudad = geoname[1] # Primer hijo
	cadena=""
	for e in ciudad:
		if (e.tag == 'name'):
			cadena=cadena+e.text+" "
		if (e.tag == 'lat'):
			cadena=cadena+e.text+" "
		if (e.tag == 'lng'):
			cadena=cadena+e.text+" "
			print (cadena)

	linea=infile.readline()

infile.close()

# Los elementos funcionan como listas
    




