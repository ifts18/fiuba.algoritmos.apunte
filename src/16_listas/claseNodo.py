class Nodo:
    """ Un nodo para formar una lista enlazada. """
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)


def verLista(nodo):
    """ Recorre todos los nodos a través de sus enlaces,
        mostrando sus contenidos. """

    # cicla mientras nodo no es None
    while nodo:
        # muestra el dato
        print(nodo)
        # ahora nodo apunta a nodo.prox
        nodo = nodo.prox
