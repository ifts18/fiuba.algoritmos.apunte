#!/usr/bin/env python
# encoding: latin1

def busqueda_con_index(xs, x):
    """Busca un elemento x en una lista xs

    si x está en xs devuelve xs.index(x)
    de lo contrario devuelve -1
    """

    if x in xs:
        return(xs.index(x))
    else:
        return(-1)

