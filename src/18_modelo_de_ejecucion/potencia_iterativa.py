#!/usr/bin/env python
# encoding: utf-8

def potencia(b,n):
	""" Precondición: n debe ser mayor o igual que cero.
	    Devuelve: b^n. """

	pila = []
	while n > 0:
		if n % 2 == 0:
			pila.append(True)
			n /= 2
		else:
			pila.append(False)
			n = (n-1)/2

	pot = 1
	while pila:
		es_par = pila.pop()
		if es_par:
			pot = pot * pot
		else:
			pot = pot * pot * b

	return pot
