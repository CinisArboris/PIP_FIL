# -*- coding: utf-8 -*-
# Vargas Medina Eyver Emilio - 213128780
import math


# -------------------------------------------------
def filtro01(cadena):
	# cada letra mayúscula o minúscula
	# debe desplazarse tres posiciones hacia la derecha
	resultado = filtro02(cadena, 3, 0, False)

	resultado = resultado[::-1]
	
	
	mitad = int(len(resultado)/2)
	p1 = resultado[:mitad]
	p2 = resultado[mitad:]
	# la mitad en adelante (truncado)
	# deben moverse una posición a la izquierda
	p2 = filtro02(p2, 1, 1, True)
	
	resultado = p1+p2
	return resultado
# -------------------------------------------------
def rotacion(cadena, posiciones, orientacion, codigo):
	# [orientacion] == 0 , derecha
	# [orientacion] == 1 , izquierda
	resultado = ''
	for cadA in cadena:
		if (
			((ord(cadA) >= ord('a')) and (ord(cadA) <= ord('o')))
			or
			((ord(cadA) >= ord('p')) and (ord(cadA) <= ord('z')))
			or
			((ord(cadA) >= ord('A')) and (ord(cadA) <= ord('O')))
			or
			((ord(cadA) >= ord('P')) and (ord(cadA) <= ord('Z')))
			or
			codigo
		):
			varA = cadA			#string
			varB = ord(cadA)	#decimal
			varC = chr(varB)	#string
			if (orientacion == 0): varB = varB + posiciones	#decimal +3
			if (orientacion == 1): varB = varB - posiciones	#decimal +3
			varA = chr(varB)	#string +3
			resultado = resultado + varA
		else:
			resultado = resultado + cadA
	return resultado
# -------------------------------------------------
def procesar_lineas_entrada(vectorLineas):
	vector_aux = []
	for linea in vectorLineas:
		vector_aux.append(rotar_linea(linea))
	# tipo = 0 :: rotacion derecha
	# tipo = 1 :: rotacion izquierda
	# movi = n :: cantidad del desplazamiento
	tipo = 0
	movi = 3	
	#rotacion(vectorLineas, tipo, movi)
	exit()
# -------------------------------------------------	
def mostrar_mensaje(cadena):
	print (cadena)
	print ('*'*40)
# -------------------------------------------------
def verif_long_lineas_de_entrada(string_alfanumerico):
	entradaMIN = 1
	entradaMAX = 3
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
def verificar_cant_lineas(nro_lineas):
	entradaMIN = 1
	entradaMAX = 3
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
def lineas_de_entrada(nro_lineas):
	vectorLineas = []
	linea = 0
	bandera = False
	while (linea < nro_lineas):
		string_alfanumerico = input('Linea '+str(linea)+'     :: ')
		bandera = verif_long_lineas_de_entrada(string_alfanumerico)
		if (bandera):
			linea = linea + 1
			bandera = False
			vectorLineas.append(string_alfanumerico)
	procesar_lineas_entrada(vectorLineas)
# -------------------------------------------------
def cantidad_lineas():
	bandera = False
	while (not bandera):
		nro_lineas = input('[nro_lineas]     :: ')
		bandera = verificar_cant_lineas(nro_lineas)
	nro_lineas = int(nro_lineas)
	lineas_de_entrada(nro_lineas)
# **************************************************
# ******************  M  A  I  N
cantidad_lineas()


