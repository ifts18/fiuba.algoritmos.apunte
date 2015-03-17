#! /usr/bin/env python
# encoding: utf-8

""" Mide el tiempo de las funciones de busquedas especificadas en el
    diccionario_funciones, todas las funciones de busquedas a medir deben
    recibir dos parámetros: el primero la lista donde se realiza la búsqueda y
    el segundo el elemento a buscar.

    El módulo provee dos funciones, una para pruebas de busquedas exitosas y
    otra para búsquedas no exitosas. Resulta curioso ver que la función de
    búsqueda busConIndex, que utiliza el operador in, presenta mejor
    perfomance en el caso de búsquedas no exitosas.
"""

import medirTiempos

# funciones de busquedas a testear:
# El diccionario_funciones contiene como claves los nombres de las funciones,
# y como valores, los archivos donde se encuentran definidas dichas funciones.
diccionario_funciones = {"busb": "busb.py",
                         "busb1": "busb1.py",
                         "busConIndex": "busConIndex.py",
                         "busl": "busl.py"}

# diccionario_funciones= {"busb": "busquedas.py",
#                         "busb1": "busquedas.py",
#                         "busConIndex": "busquedas.py",
#                         "busl": "busquedas.py"}


def _medir_busquedas(inicio, fin, paso, encontrado):
    'Función que realmente realiza las mediciones'
    resultados = {}
    for n in range(inicio, fin, paso):
        xs = range(n)
        if encontrado:
            elemento = n - 1
        else:
            elemento = n
        res = {}
        for funcion in diccionario_funciones.keys():
            res[funcion] = medirTiempos.medir_tiempos(
                funcion, [xs, elemento], diccionario_funciones[funcion])
        resultados[n] = res
    return resultados


def medir_busquedas_exitosas(inicio, fin, paso=1):
    """ Esta función mide búsquedas exitosas, para lo cual se genera una
        lista ordenada (para poder aplicar búsqueda binaria) y se busca el
        último elemento de la lista (Es decir el peor caso).

        Las mediciones se realizan con tamaños de entrada que van desde inicio
        hasta fin, con saltos indicados por paso.

    Pre:
        inicio: Tamaño inicial de la lista ordenada, sobre la que
                se realizarán las busquedas. Si es 0, indica la lista
                vacia.

        fin:    Tamaño final de la lista ordenada, para pruebas.

        paso:   Incrementos en el tamaño de la lista ordenada, para
                ir desde inicio hasta fin. Si se omite toma 1

    Post:
        Devuelve un diccionario, cuyas claves son los tamaños de las
        entradas usadas en las mediciones, y cuyos valores son
        otros diccionarios.
        En estos otros diccionarios las claves son los nombres de las
        funciones y los valores los tiempos medidos.

    Ejemplo de diccionario:
        {0: {busb: 0.134872,
             busb1: 0.139061,
             busl: 0.087852,
             busConIndex: 0.073662},
         1: {busb: 0.191309,
             busb1: 0.195972,
             busl: 0.129301,
             busConIndex: 0.171993}}
    """

    return _medir_busquedas(inicio, fin, paso, True)


def medir_busquedas_no_exitosas(inicio, fin, paso=1):
    """ Esta función mide búsquedas no exitosas, para lo cual se genera una
        lista ordenada (para poder aplicar busqueda binaria) y se busca
        un elemento mayor al ultimo de la lista (Es decir el peor caso).
        Las mediciones se realizan con tamaños de entrada que van desde inicio
        hasta fin, con saltos indicados por paso.

    Pre:
        inicio: Tamaño inicial de la lista ordenada, sobre la que
                se realizaran las búsquedas. Si es 0, indica la lista
                vacia.

        fin:    Tamaño final de la lista ordenada, para pruebas.

        paso:   Incrementos en el tamaño de la lista ordenada, para
                ir desde inicio hasta fin. Si se omite, toma 1

    Post:
        Devuelve un diccionario, cuyas claves son los tamaños de las
        entradas usadas en las mediciones, y cuyos valores son
        otros diccionarios.
        En estos otros diccionarios las claves son los nombres de las
        funciones y los valores los tiempos medidos.

    Ejemplo de diccionario:
        {0: {busb: 0.134700,
             busb1: 0.13871,
             busl: 0.087819,
             busConIndex: 0.072686},
         1: {busb: 0.206518,
             busb1: 0.175428,
             busl: 0.145051,
             busConIndex: 0.096389}}
    """

    return _medir_busquedas(inicio, fin, paso, False)


if __name__ == "__main__":

    print "Busquedas Exitosas"
    resultados = medir_busquedas_exitosas(0, 10, 1)
    for res in sorted(resultados):
        print "Resultados con n=%d" % res
        for funcion in resultados[res].keys():
            print "archivo: %s\nfuncion: %s\n%f\n" % (
                diccionario_funciones[funcion], funcion,
                resultados[res][funcion])
        print "\n\n"

    print "Busquedas No Exitosas"
    resultados = medir_busquedas_no_exitosas(0, 10, 1)
    for res in sorted(resultados):
        print "Resultados con n=%d" % res
        for funcion in resultados[res].keys():
            print "archivo: %s\nfuncion: %s\n%f\n" % (
                diccionario_funciones[funcion], funcion,
                resultados[res][funcion])
        print "\n\n"
