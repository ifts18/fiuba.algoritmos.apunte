def quick_sort(lista):
    """Ordena la lista de forma recursiva.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada. """
    _quick_sort(lista, 0, len(lista) - 1)

def _quick_sort(lista, inicio, fin):
    """Función quick_sort recursiva.
       Pre: los índices inicio y fin indican sobre qué porción operar.
       Post: la lista está ordenada."""
    if inicio >= fin:
        return
    menores = _partition(lista, inicio, fin)
    _quick_sort(lista, inicio, menores - 1)
    _quick_sort(lista, menores + 1, fin)

def _partition(lista, inicio, fin):
    """Función partición que trabaja sobre la misma lista.
       Pre: los índices inicio y fin indican sobre qué porción operar.
       Post: los menores están antes que el pivote, los mayores después.
       Devuelve: la posición en la que quedó ubicado el pivote."""
    pivote = lista[inicio]
    menores = inicio

    # Ubicar menores a la izquierda, mayores a la derecha
    for i in range(inicio + 1, fin + 1):
        if lista[i] < pivote:
            menores += 1
            if i != menores:
                _swap(lista, i, menores)
    # Ubicar el pivote al final de los menores
    if inicio != menores:
        _swap(lista, inicio, menores)
    return menores

def _swap(lista, i, j):
    """Intercambia los elementos i y j de lista."""
    lista[j], lista[i] = lista[i], lista[j]
