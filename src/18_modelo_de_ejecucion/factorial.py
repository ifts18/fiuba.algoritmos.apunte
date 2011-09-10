#!/usr/bin/env python
#encoding: latin1

def factorial(n):
    """ Precondición: n entero >=0
        Devuelve: n! """
    if n == 0:
        return 1

    return n * factorial(n-1)
