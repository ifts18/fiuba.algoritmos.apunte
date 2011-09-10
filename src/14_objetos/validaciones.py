#!/usr/bin/env python
#encoding: latin1

""" Módulo para realizar validaciones. """

def es_numero(valor):
    """ Indica si un valor es numérico o no. """ 
    return isinstance(valor, (int, float, long, complex) )

def es_cadena_no_vacia(valor):
    """ Verifica que el valor sea una cadena no vacía. """
    if not isinstance(valor, basestring):
        return False
    else:
        return len(valor)>0
