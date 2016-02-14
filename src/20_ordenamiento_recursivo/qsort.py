def swap(l, i, j):
    print("intercambiando {}, {} ".format((i, j), l)
    l[j], l[i] = l[i], l[j]

def quick_sort(lista, inicio, fin):
    if (fin - inicio) < 1:
        return

    menores = inicio
    pivote = lista[inicio]

    for i in range(inicio+1, fin+1):
        if lista[i] < pivote:
            menores += 1
            if i != menores:
                swap(lista, i, menores)

    if inicio != menores:
        swap(lista, inicio, menores)

    quick_sort(lista, inicio, menores-1)
    quick_sort(lista, menores+1, fin)

def qsort(lista):
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

def py_qsort(l):
    if len(l) <= 1:
        return l
    menores = py_qsort( [x for x in l[1:] if x < l[0]] )
    mayores = py_qsort( [x for x in l[1:] if x >= l[0] ] )
    return menores + l[0:1] + mayores

