# -*- coding: utf-8 -*-
# Vargas Medina Eyver Emilio - 213128780

# -------------------------------------------------
def unir(vector_parte_a, vector_parte_b):
	vector_resultado = []
	# len vpa = vpb
	repeticion = len(vector_parte_a)
	for it in range(repeticion):
		vector_resultado.append(
				str(vector_parte_a[it]) +
				str(vector_parte_b[it])
			)
	mostrar_mensaje(vector_resultado)
# -------------------------------------------------
def rotar_lineas_2(vectorLineas, rotacion, movi):
	vectorLineas_tmp = []
	letra_tmp = ''
	for linea in vectorLineas:
		letra_tmp = ''
		for letra in linea:
			# rotacion :: [0=derecha][1=izquierda]
			# movi = n :: cantidad del desplazamiento
			if (rotacion == 0): letra_tmp = letra_tmp + chr(ord(letra) + movi)
			if (rotacion == 1): letra_tmp = letra_tmp + chr(ord(letra) - movi)
		vectorLineas_tmp.append(letra_tmp)
		#print ('letra_tmp', letra_tmp)
	vectorLineas = vectorLineas_tmp
	return vectorLineas
# -------------------------------------------------
def separar(vectorLineas):
	vector_parte_a = []
	vector_parte_b = []	
	
	for cadena in vectorLineas:
		mitad = int(len(cadena)/2)
		vector_parte_a.append(cadena[:mitad]) # ab
		vector_parte_b.append(cadena[mitad:]) # cd
	#print ('separar', 'vector_parte_a', vector_parte_a)
	#print ('separar', 'vector_parte_b', vector_parte_b)
	# rotacion :: [0=derecha][1=izquierda]
	# movi = n :: cantidad del desplazamiento
	rotacion = 1
	movi = 1
	vector_parte_b = rotar_lineas_2(vector_parte_b, rotacion, movi)
	#print ('separar', 'vector_parte_b', vector_parte_b)
	#exit()
	unir(vector_parte_a, vector_parte_b)
# -------------------------------------------------
def invertir(vectorLineas):
	vectorLineas_tmp = []
	for linea in vectorLineas:
		vectorLineas_tmp.append(linea[::-1])
	vectorLineas = vectorLineas_tmp
	return vectorLineas
# -------------------------------------------------
def rotar_lineas(vectorLineas, rotacion, movi):
	vectorLineas_tmp = []
	letra_tmp = ''
	#print ('rotar_lineas', 'antes', vectorLineas)
	for linea in vectorLineas:
		letra_tmp = ''
		for letra in linea:
			if (
				((ord(letra) >= ord('a')) and (ord(letra) <= ord('o')))
				or
				((ord(letra) >= ord('p')) and (ord(letra) <= ord('z')))
				or
				((ord(letra) >= ord('A')) and (ord(letra) <= ord('O')))
				or
				((ord(letra) >= ord('P')) and (ord(letra) <= ord('Z')))
			):
				# rotacion :: [0=derecha][1=izquierda]
				# movi = n :: cantidad del desplazamiento
				if (rotacion == 0): letra_tmp = letra_tmp + str(chr(ord(letra) + movi))
				if (rotacion == 1): letra_tmp = letra_tmp + str(chr(ord(letra) - movi))
			else:
				letra_tmp = letra_tmp + letra
		vectorLineas_tmp.append(letra_tmp)
		#print ('letra_tmp', letra_tmp)
	vectorLineas = vectorLineas_tmp
	#print ('rotar_lineas', 'despu', vectorLineas)
	#return vectorLineas
	vectorLineas = invertir(vectorLineas)
	#print ('rotar_lineas', 'inver', vectorLineas)
	#exit()
	separar(vectorLineas)
# -------------------------------------------------
def procesar_lineas_entrada(vectorLineas):
	vector_aux = []
	# rotacion :: [0=derecha][1=izquierda]
	# movi = n :: cantidad del desplazamiento
	rotacion	= 0
	movi		= 3
	rotar_lineas(vectorLineas, rotacion, movi)
# -------------------------------------------------
def verificar_longitud_lineas_entrada(string_alfanumerico):
	entradaMIN = 1
	entradaMAX = 100
	longitud_actual = len(string_alfanumerico)
	bandera = True
	if (longitud_actual < entradaMIN):
		mensaje = '[string_alfanumerico] debe ser mínimo: ' + str(entradaMIN)
		mostrar_mensaje(mensaje)
		bandera = False
	if (longitud_actual > entradaMAX):
		mensaje = '[string_alfanumerico] debe ser máximo: ' + str(entradaMAX)
		mostrar_mensaje(mensaje)
		bandera = False
	return bandera
# -------------------------------------------------
def lineas_entrada(nro_lineas):
	vectorLineas = []
	linea = 0
	bandera = False
	while (linea < nro_lineas):
		string_alfanumerico = input('Linea '+str(linea)+'     :: ')
		bandera = verificar_longitud_lineas_entrada(string_alfanumerico)
		if (bandera):
			linea = linea + 1
			bandera = False
			vectorLineas.append(string_alfanumerico)
	procesar_lineas_entrada(vectorLineas)
# -------------------------------------------------
def mostrar_mensaje(cadena):
	print (cadena)
	print ('*'*40)
# -------------------------------------------------
def verificar_cantidad_lineas(nro_lineas):
	entradaMIN = 1
	entradaMAX = 10
	mensaje = ''
	bandera = True
	if (not nro_lineas.isnumeric()):
		mensaje = '[nro_lineas] debe ser numérico.'
		mostrar_mensaje(mensaje)
		bandera = False
	else:
		nro_lineas = int(nro_lineas)
		if (nro_lineas < entradaMIN):
			mensaje = '[nro_lineas] debe ser mínimo: ' + str(entradaMIN)
			mostrar_mensaje(mensaje)
			bandera = False
		if (nro_lineas > entradaMAX):
			mensaje = '[nro_lineas] debe ser máximo: ' + str(entradaMAX)
			mostrar_mensaje(mensaje)
			bandera = False
	return bandera
# -------------------------------------------------
def cantidad_lineas():
	bandera = False
	while (not bandera):
		nro_lineas = input('[nro_lineas]     :: ')
		bandera = verificar_cantidad_lineas(nro_lineas)
	nro_lineas = int(nro_lineas)
	lineas_entrada(nro_lineas)
# **************************************************
# ******************  M  A  I  N
cantidad_lineas()


