#/usr/bin/env python
# encoding: utf-8

def ord_seleccion(lista):
    """ Ordena una lista de elementos según el método de selección.
        Pre: los elementos de la lista deben ser comparables.
        Post: la lista está ordenada. """

    # n = posicion final del segmento a tratar, comienza en len(lista)-1
    n = len(lista)-1

    # cicla mientras haya elementos para ordenar (2 o más elementos)
    while n > 0:

        # p es la posicion del mayor valor del segmento
        p = buscar_max(lista, 0, n)

        # intercambia el valor que está en p con el valor que 
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]

        print "DEBUG: ", p, n, lista

        # reduce el segmento en 1
        n = n - 1

def buscar_max(lista, ini, fin):
    """ Devuelve la posición del máximo elemento en un segmento de
        lista de elementos comparables.  
        Se trabaja sobre lista, que no debe ser vacía.
        ini es la posición inicial del segmento, debe ser válida.
        fin es la posición final del segmento, debe ser válida. """
        
    pos_max = ini
    for i in xrange(ini+1, fin+1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max
