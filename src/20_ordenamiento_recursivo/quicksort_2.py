
def qsort(lista):
    """ Otra implementación de quicksort. """
    def _qsort(lista, inicio, fin):
        if inicio >= fin:
            return
        pivote = inicio
        menores = inicio + 1
        mayores = fin
        while menores <= mayores:
            if lista[pivote] <= lista[mayores]:
                mayores -= 1
            elif lista[menores] < lista[pivote]:
                menores += 1
            else:
                lista[mayores], lista[menores] = lista[menores], lista[mayores]
        menores -= 1
        lista[menores], lista[pivote] = lista[pivote], lista[menores]
        _qsort(lista, inicio, menores-1)
        _qsort(lista, menores+1, fin)

    _qsort(lista, 0, len(lista)-1)
