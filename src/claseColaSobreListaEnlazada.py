import claseListaEnlazadaConUlt

class Cola:
    """ cola comun implementada sobre lista enlazada"""
    def __init__(self):

        """ crea una cola vacia
          representada por una lista enlazada vacia"""
        self.items=claseListaEnlazadaConUlt.ListaEnlazada()

    def encolar(self, x):
        """ encola x en self
            (lo agrega al final de la lista)"""
        self.items.append(x)

    def desencolar(self):
        """ elimina el primer elemento de la
            lista y retorna su valor.
            Si la cola esta vacia se devolvera None."""

        try:
            return self.items.pop(0)
        except:
            return None
    def esColaVacia(self):
        """ devuelve True si la cola esta vacia,
            False en caso contrario."""

        return (self.items.__len__() == 0)
