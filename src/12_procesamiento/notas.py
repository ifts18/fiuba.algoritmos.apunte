#!/usr/bin/env python
# encoding: utf-8
import csv

def leer_datos(datos):
	""" Obtiene el siguiente registro, o devuelve None si llegó al fin
	    del archivo. """
	try:
		return datos.next()
	except:
		return None

def imprimir_notas_alumnos(alumnos, notas):
	""" Abre los archivos de alumnos y notas, y por cada alumno imprime
	    todas las notas que le corresponden. """
	notas_a = open(notas)
	alumnos_a = open(alumnos)
	notas_csv = csv.reader(notas_a)
	alumnos_csv = csv.reader(alumnos_a)

	# Saltea los encabezados
	leer_datos(notas_csv)
	leer_datos(alumnos_csv)

	# Empieza a leer
	alumno = leer_datos(alumnos_csv)
	nota = leer_datos(notas_csv)
	while (alumno):
		print alumno[2]+", "+alumno[1]+" - "+alumno[0]
		if (not nota or nota[0] != alumno[0]):
			print "\tNo se registran notas"
		while (nota and nota[0] == alumno[0]):
			print "\t"+nota[1]+": "+nota[2]
			nota = leer_datos(notas_csv)
		alumno = leer_datos(alumnos_csv)

	# Cierro los archivos
	notas_a.close()
	alumnos_a.close()

imprimir_notas_alumnos("alumnos.csv", "notas.csv")
