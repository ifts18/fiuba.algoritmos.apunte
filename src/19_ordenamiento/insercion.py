#!/usr/bin/env python
#encoding: latin1

def ord_insercion(lista):
    """ Ordena una lista de elementos según el método de inserción.
        Pre: los elementos de la lista deben ser comparables.
        Post: la lista está ordenada. """

    # i va desde la primera hasta la penúltima posición de la lista
    for i in xrange(len(lista)-1):

        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i+1]< lista[i]:
            reubicar(lista, i+1)

        print "DEBUG: ", lista

def reubicar(lista, p):
    """ Reubica al elemento que está en la posición p de la lista 
        dentro del segmento [0:p-1].
        Pre: p tiene que ser una posicion válida de lista. """

    # v es el valor a reubicar
    v = lista[p]

    # Recorre el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p 
    while j > 0 and v < lista[j-1]:
		# Desplaza los elementos hacia la derecha, dejando lugar
		# para insertar el elemento v donde corresponda.
        lista[j] = lista[j-1]
		# Se mueve un lugar a la izquierda
        j -= 1

    # Ubica el valor v en su nueva posición
    lista[j] = v
