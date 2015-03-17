#!/usr/bin/env python
# encoding: utf-8

def merge_sort(lista):
    """ Ordena lista mediante el método merge sort.
        Pre: lista debe contener elementos comparables.
        Devuelve: una nueva lista ordenada. """

    # Una lista de 1 o 0 elementos, ya está ordenada
    if len(lista) < 2:
        return lista
    # Si tiene 2 o más elementos, se divide al medio y ordena cada parte
    medio = len(lista) / 2
    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])
    return merge(izq, der)

def merge(lista1, lista2):
    """ Intercala los elementos de lista1 y lista2 de forma ordenada.
        Pre: lista1 y lista2 deben estar ordenadas.
        Devuelve: una lista con los elementos de lista1 y lista2. """

    i, j = 0, 0
    resultado = []

    # Intercalar ordenadamente
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta, si i o j ya son len(lista) no agrega nada.
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado
