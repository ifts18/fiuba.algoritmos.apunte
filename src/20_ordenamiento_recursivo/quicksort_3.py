#/usr/bin/env python
# encoding: utf-8

def py_qsort(l):
    """ Otra implementación de quicksort, devuelve una nueva lista. """
    if len(l) <= 1:
        return l
	# Separa en menores y mayores mediante listas por comprensión
    menores = py_qsort( [x for x in l[1:] if x < l[0]] )
    mayores = py_qsort( [x for x in l[1:] if x >= l[0] ] )
    return menores + l[0:1] + mayores

