#! /usr/bin/env Python
# encoding: utf-8

from claseNodo import Nodo

class Cola:
    """ Representa a una cola, con operaciones de encolar y
        desencolar.  El primero en ser encolado es también el primero
        en ser desencolado. """

    def __init__(self):
        """ Crea una cola vacía. """
        # En el primer momento, tanto el primero como el último son None
        self.primero = None
        self.ultimo = None

    def encolar(self, x):
        """ Agrega el elemento x como último de la cola. """
        nuevo = Nodo(x)        
        # Si ya hay un último, agrega el nuevo y cambia la referencia.
        if self.ultimo:
            self.ultimo.prox = nuevo
            self.ultimo = nuevo
        # Si la cola estaba vacía, el primero es también el último.
        else:
            self.primero = nuevo
            self.ultimo = nuevo

    def desencolar(self):
        """ Elimina el primer elemento de la cola y devuelve su 
            valor. Si la cola está vacía, levanta ValueError. """
        # Si hay un nodo para desencolar
        if self.primero:
            valor = self.primero.dato
            self.primero = self.primero.prox
            # Si después de avanzar no quedó nada, también hay que
            # eliminar la referencia del último.
            if not self.primero:
                self.ultimo = None
            return valor
        else:
            raise ValueError("La cola está vacía")

    def es_vacia(self):
        """ Devuelve True si la cola esta vacía, False si no."""
        return self.primero == None
