#!/usr/bin/env python
# encoding: utf-8

def factorial(n):
    """ Precondición: n entero >=0
        Devuelve: n! """

	fact = 1
	for num in xrange(n, 1, -1):
		fact *= num
	return fact
