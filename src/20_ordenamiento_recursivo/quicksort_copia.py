def quick_sort(lista):
    """Ordena la lista de forma recursiva.
       Pre: los elementos de la lista deben ser comparables.
       Devuelve: una nueva lista con los elementos ordenados."""
    if len(lista) < 2:
        return lista
    menores, medio, mayores = _partition(lista)
    return quick_sort(menores) + medio + quick_sort(mayores)

def _partition(lista):
    """Pre: lista no vacía.
       Devuelve: tres listas: menores, medio y mayores."""
    pivote = lista[0]
    menores = []
    mayores = []
    for x in range(1, len(lista)):
        if lista[x] < pivote:
            menores.append(lista[x])
        else:
            mayores.append(lista[x])
    return menores, [pivote], mayores
