# -*- coding: utf-8 -*-
import math
import tkinter
# Vargas Medina Eyver Emilio
# 213128780

# -------------------------------------------------
def filtro02(cadena, posiciones, orientacion, codigo):
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
# Mostrar los resultados en un Label
def mostrar_mensaje(cadena):
	print (cadena)
	print ('*'*40)
# -------------------------------------------------
def verificar_longitud_linea(string_alfanumerico):
	entradaMIN = 1
	entradaMAX = 3
	longitud_actual = len(string_alfanumerico)
	bandera = True
	if (longitud_actual < entradaMIN):
		mensaje = '[string_alfanumerico] debe ser mayor: ' + str(entradaMIN)
		mostrar_mensaje(mensaje)
		bandera = False
	if (longitud_actual > entradaMAX):
		mensaje = '[string_alfanumerico] debe ser menor: ' + str(entradaMAX)
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
			mensaje = '[nro_lineas] debe ser mayor: ' + str(entradaMIN)
			mostrar_mensaje(mensaje)
			bandera = False
		if (nro_lineas > entradaMAX):
			mensaje = '[nro_lineas] debe ser menor: ' + str(entradaMAX)
			mostrar_mensaje(mensaje)
			bandera = False
	return bandera
# -------------------------------------------------
def contenedor():
	bandera = False
	while (not bandera):
		# parte 01
		nro_lineas = input('[nro_lineas]     :: ')
		bandera = verificar_cant_lineas(nro_lineas)
	nro_lineas = int(nro_lineas)
	
	# parte 02
	print ('-'*20)
	vectorLineas = []
	linea = 0
	bandera = False
	while (linea < nro_lineas):
		string_alfanumerico = input('Linea '+str(linea)+'     :: ')
		bandera = verificar_longitud_linea(string_alfanumerico)
		if (bandera):
			linea = linea + 1
			bandera = False
			vectorLineas.append(string_alfanumerico)
	# parte 03
	print ('-'*20)
	
	print ('='*20, 'EXIT')
	print ('vectorLineas', vectorLineas)
# **************************************************
# ******************  M  A  I  N
contenedor()


