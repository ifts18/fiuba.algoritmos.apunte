#! /usr/bin/env python
# encoding: utf-8

import pickle

def guardar_puntajes(nombre_archivo, puntajes):
    """ Guarda la lista de puntajes en el archivo.
    Pre: nombre_archivo corresponde a un archivo válido,
         puntajes corresponde a los valores a guardar
    Post: se guardaron los valores en el archivo en formato pickle.
    """

    archivo = open(nombre_archivo, "w")
    pickle.dump(puntajes, archivo)
    archivo.close()

def recuperar_puntajes(nombre_archivo):
    """ Recupera los puntajes a partir del archivo provisto.
        Devuelve una lista con los valores de los puntajes.
    Pre: el archivo contiene los puntajes en formato pickle
    Post: la lista devuelta contiene los puntajes en el
          mismo formato que se los almacenó.
    """

    archivo = open(nombre_archivo, "r")
    puntajes = pickle.load(archivo)
    archivo.close()
    return puntajes
