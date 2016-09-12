def busqueda_binaria(lista, x):
    """Búsqueda binaria

    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    """

    izq = 0
    der = len(lista) - 1

    while izq <= der:
        medio = (izq + der) // 2
        print("[DEBUG]", "izq:", izq, "der:", der, "medio:", medio)

        if lista[medio] == x:
            # Encontramos el elemento; devolvemos su posición
            return medio

        if lista[medio] > x:
            # Seguimos buscando en el segmento de la izquierda
            der = medio - 1
        else:
            # Seguimos buscando en el segmento de la derecha
            izq = medio + 1

    # El valor no fue encontrado
    return -1
