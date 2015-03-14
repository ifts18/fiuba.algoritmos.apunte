#! /usr/bin/env python
# encoding: utf-8

def guardar_puntajes(nombre_archivo, puntajes):
    """ Guarda la lista de puntajes en el archivo.
    Pre: nombre_archivo corresponde a un archivo válido,
         puntajes corresponde a una lista de tuplas de 3 elementos.
    Post: se guardaron los valores en el archivo, 
          separados por comas.
    """

    archivo = open(nombre_archivo, "w")
    for nombre, puntaje, tiempo in puntajes:
    	archivo.write(nombre+","+str(puntaje)+","+tiempo+"\n")
    archivo.close()

def recuperar_puntajes(nombre_archivo):
    """ Recupera los puntajes a partir del archivo provisto.
    	Devuelve una lista con los valores de los puntajes.
    Pre: el archivo contiene los puntajes en el formato esperado, 
         separados por comas
    Post: la lista devuelta contiene los puntajes en el formato:
          [(nombre1,puntaje1,tiempo1),(nombre2,puntaje2,tiempo2)]. 
    """

    puntajes = []
    archivo = open(nombre_archivo, "r")
    for linea in archivo:
    	nombre, puntaje, tiempo = linea.rstrip("\n").split(",")
    	puntajes.append((nombre,int(puntaje),tiempo))
    archivo.close()
    return puntajes
