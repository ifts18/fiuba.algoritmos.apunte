#!/usr/bin/env python
# encoding: utf-8

def busqueda_binaria(lista, x):
    """Búsqueda binaria
    Precondición: lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    """

    # Busca en toda la lista dividiéndola en segmentos y considerando
    # a la lista completa como el segmento que empieza en 0 y termina
    # en len(lista) - 1.

    izq = 0              # izq guarda el índice inicio del segmento
    der = len(lista) - 1 # der guarda el índice fin del segmento

    # un segmento es vacío cuando izq > der:
    while izq <= der:
        # el punto medio del segmento
        medio = (izq+der)/2

        print "DEBUG:", "izq:", izq, "der:", der, "medio:", medio

        # si el medio es igual al valor buscado, lo devuelve
        if lista[medio] == x:
            return medio
        # si el valor del punto medio es mayor que x, sigue buscando
        # en el segmento de la izquierda: [izq, medio-1], descartando la
        # derecha
        elif lista[medio] > x:
            der = medio-1
        # si no, sigue buscando en el segmento de la derecha:
        # [medio+1, der], descartando la izquierda
        else:
            izq = medio+1
        # si no salió del ciclo, vuelve a iterar con el nuevo segmento

    # salió del ciclo de manera no exitosa: el valor no fue encontrado
    return -1

# Código para probar la búsqueda binaria
def main():
    lista = input ("Dame una lista ordenada ([[]] para terminar): ")
    while lista != [[]]:
        x = input("¿Valor buscado?: ")
        resultado = busqueda_binaria(lista, x)
        print "Resultado:", resultado
        lista = input ("Dame una lista ordenada ([[]] para terminar): ")

main()
