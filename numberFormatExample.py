def numberFormat( numero ):
	cadena = str( numero )
	indice = len( cadena )
	while indice > 3:
		indice = indice - 3
		cadena = cadena[ :indice ] + ',' + cadena[ indice: ]
	return cadena

print numberFormat(109876543738)


