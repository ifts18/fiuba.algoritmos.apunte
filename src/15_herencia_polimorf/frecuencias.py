#!/usr/bin/env python
# encoding: utf-8

def frecuencias(secuencia):
    """ Calcula las frecuencias de aparición de los elementos de
        la secuencia recibida.
        Devuelve un diccionario con elementos: {valor: frecuencia}
    """
    # crea un diccionario vacío
    frec = dict()
    # recorre la secuencia
    for elemento in secuencia:
        frec[elemento] = frec.get(elemento, 0) + 1

    return frec

