#!/usr/bin/env python
# encoding: utf-8

def quick_sort(lista):
	""" Una posible implementación de quick sort. """
	_quick_sort(lista, 0, len(lista)-1)

def _quick_sort(lista, inicio, fin):

	# Caso base
	if inicio >= fin:
		return

	# Caso recursivo
	q = _partition(lista, inicio, fin)
	_quick_sort(lista, inicio, q-1)
	_quick_sort(lista, q+1, fin)

def _partition(lista, inicio, fin):

	# Optimización para listas ordenadas, cambia el medio con el inicio
	m = ( inicio + fin ) / 2
	_swap(lista, m, inicio)	

	p, i, j = inicio, inicio+1, fin
	
	while i <= j:
		# Saltea todos los que ya están correctamente ubicados
		while i <= j and lista[i] < lista[p]:
			i+=1
		while i <= j and lista[j] >= lista[p]:
			j-=1
		# intercambia el elemento i con el j
		if i < j: 
			_swap(lista, i, j)

	# Una vez que todos están correctamente ubicados, pone el pivote en el medio
	q = min(i,j)
	_swap(lista, p, q)

	return q

def _swap(lista, i, j):
	lista[i], lista[j] = lista[j], lista[i]
	
