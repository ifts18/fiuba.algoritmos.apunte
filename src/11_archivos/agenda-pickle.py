#!/usr/bin/env python
# encoding: utf-8

import pickle

ARCHIVO="agenda.dat"

def leer_datos(archivo):
	""" Carga todos los datos del archivo en una lista y la devuelve. """
	abierto = open(archivo)
	datos = pickle.load(archivo)
	abierto.close()
	return datos

def guardar_datos(datos, archivo):
	""" Guarda los datos recibidos en el archivo. """
	abierto = open(archivo,"w")
	pickle.dump(archivo, datos)
	abierto.close()

def leer_busqueda():
	""" Solicita al usuario nombre y apellido y los devuelve. """
	nombre = raw_input("Nombre: ")
	apellido = raw_input("Apellido: ")
	return (nombre,apellido)

def buscar(nombre, apellido, datos):
	""" Busca el primer elemento que coincida con nombre y con apellido. """
	for elemento in datos:
		if nombre in elemento[0] and apellido in elemento[1]:
			return elemento
	return None

def menu_alta(nombre, apellido, datos):
	""" Pregunta si se desea ingresar un nombre y apellido y
        de ser así, pide los datos al usuario. """
	print "No se encuentra %s %s en la agenda." % (nombre, apellido)
	confirmacion = raw_input("¿Desea ingresarlo? (s/n) ")
	if confirmacion.lower() != "s":
		return
	telefono = raw_input("Telefono: ")
	cumple = raw_input("Cumpleaños: ")
	datos.append([nombre,apellido,telefono,cumple])

def mostrar_elemento(elemento):
	""" Muestra por pantalla un elemento en particular. """
	print
	print "%s %s" % (elemento[0],elemento[1])
	print "Telefono: %s" % elemento[2]
	print "Cumpleaños: %s" % elemento[3]
	print

def menu_elemento():
	""" Muestra por pantalla las opciones disponibles para un elemento
	    existente. """
	o = raw_input("b: borrar, m: modificar, ENTER para continuar (b/m): ")
	return o.lower()

def modificar(viejo, nuevo, datos):
	""" Reemplaza el elemento viejo con el nuevo, en la lista datos. """
	indice = datos.index(viejo)
	datos[indice] = nuevo

def menu_modificacion(elemento, datos):
	""" Solicita al usuario los datos para modificar una entrada. """
	nombre = raw_input("Nuevo nombre: ")
	apellido = raw_input("Nuevo apellido: ")
	telefono = raw_input("Nuevo teléfono: ")
	cumple = raw_input("Nuevo cumpleaños: ")
	modificar(elemento, [nombre, apellido, telefono, cumple], datos)

def baja(elemento, datos):
	""" Elimina un elemento de la lista. """
	datos.remove(elemento)

def confirmar_salida():
	""" Solicita confirmación para salir """
	confirmacion = raw_input("¿Desea salir? (s/n) ")
	return confirmacion.lower() == "s"

def agenda():
	""" Función principal de la agenda.
	    Carga los datos del archivo, permite hacer búsquedas, modificar
		borrar, y al salir guarda. """
	datos = leer_datos(ARCHIVO)
	fin = False
	while not fin:
		(nombre, apellido) = leer_busqueda()
		if nombre == "" and apellido == "":
			fin = confirmar_salida()
			continue
		elemento = buscar(nombre, apellido, datos)
		if not elemento:
			menu_alta(nombre, apellido, datos)
			continue
		mostrar_elemento(elemento)
		opcion = menu_elemento()
		if opcion == "m":
			menu_modificacion(elemento, datos)
		elif opcion == "b":
			baja(elemento, datos)
	guardar_datos(datos, ARCHIVO)

agenda()
