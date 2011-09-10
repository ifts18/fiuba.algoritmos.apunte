#! /usr/bin/env python
# encoding: latin1

class _Nodo(object):
    """ Modela a un nodo de la lista. 
        Contiene una referencia al dato y al siguiente nodo. """
    def __init__(self, dato=None, prox = None):
        self.dato = dato
        self.prox = prox
    def __str__(self):
        return str(self.dato)

class ListaEnlazada(object):
    " Modela una lista enlazada, compuesta de Nodos. "

    def __init__(self):
        """ Crea una lista enlazada vacía. """
        # prim: apuntara al primer nodo - None con la lista vacía
        self.prim = None
        # len: longitud de la lista - 0 con la lista vacía 
        self.len = 0

    def __str__(self):
        """ Imprime el contenido de la lista. """
        nodo = self.prim
        s="["
        while nodo != None:
            if len(s) > 1: s+= ", "
            s += str(nodo)
            nodo = nodo.prox
        s += "]"
        return s

    def __len__(self):
        " Devuelve el largo de la lista. "
        return self.len

    def append(self, x):
        """ Agrega el elemento x al final de la lista. """

        # Se trata de un caso particular de insert
        self.insert(self.len, x)

    def insert(self, i, x):
        """ Inserta el elemento x en la posición i.
            Si la posición es inválida, levanta IndexError """

        if (i > self.len) or (i < 0):
            # error
            raise IndexError("Posición inválida")

        # Crea nuevo nodo, con x como dato:
        nuevo = _Nodo(x)

        # Insertar al principio (caso particular)
        if i == 0:
            # el siguiente del nuevo pasa a ser el que era primero
            nuevo.prox = self.prim
            # el nuevo pasa a ser el primero de la lista
            self.prim = nuevo

        # Insertar en cualquier lugar > 0
        else:
            # Recorre la lista hasta llegar a la posición deseada
            n_ant = self.prim
            for pos in xrange(1,i):
                n_ant = n_ant.prox

            # Intercala nuevo y obtiene n_ant -> nuevo -> n_ant.prox
            nuevo.prox = n_ant.prox
            n_ant.prox = nuevo

        # En cualquier caso, incrementar en 1 la longitud
        self.len += 1

    def remove(self, x):
        """ Borra la primera aparición del valor x en la lista.
            Si x no está en la lista, levanta ValueError """

        if self.len == 0:
            # Si la lista está vacía, no hay nada que borrar.
            raise ValueError("Lista vacía")

        # Caso particular, x esta en el primer nodo
        elif self.prim.dato == x:
            # Se descarta la cabecera de la lista
            self.prim = self.prim.prox

        # En cualquier otro caso, hay que buscar a x
        else:
            # Obtiene el nodo anterior al que contiene a x (n_ant)
            n_ant = self.prim
            n_act = n_ant.prox
            while n_act != None and n_act.dato != x:
                n_ant = n_act
                n_act = n_ant.prox

            # Si no se encontró a x en la lista, levanta la excepción
            if n_act == None:
                raise ValueError("El valor no está en la lista.")

            # Si encontró a x, debe pasar de n_ant -> n_x -> n_x.prox
            # a n_ant -> n_x.prox
            else:
                n_ant.prox = n_act.prox

        # Si no levantó excepción, hay que restar 1 del largo
        self.len -= 1

    def index(self, x):
        """ Devuelve el índice de la lista donde se encuentra la
            primera aparición de x,
           o devuelve ValueError si x no esta"""
        
        # Busca el primer nodo que contenga x
        i = 0
        n_act = self.prim
        while n_act != None and n_act.dato != x:
            n_act = n_act.prox
            i+=1
        # Si lo encontró, lo devuelve, sino levanta una excepción
        if n_act.dato == x:
            return i
        else:
            raise ValueError("El valor no se encuentra en la lista.")

        
    def pop(self, i = None):
        """ Elimina el nodo de la posición i, y devuelve el dato contenido.
            Si i está fuera de rango, se levanta la excepción IndexError.
            Si no se recibe la posición, devuelve el último elemento. """

        # Verificación de los límites
        if (i < 0) or (i >= self.len):
            raise IndexError("Índice fuera de rango")

        # Si no se recibió i, se devuelve el último.
        if i == None:
            i = self.len - 1

        # Caso particular, si es el primero, 
        # hay que saltear la cabecera de la lista
        if i == 0:
            dato = self.prim.dato
            self.prim = self.prim.prox

        # Para todos los demás elementos, busca la posición
        else:
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in xrange(1, i):
                n_ant = n_act
                n_act = n_ant.prox

            # Guarda el dato y elimina el nodo a borrar
            dato = n_act.dato
            n_ant.prox = n_act.prox

        # hay que restar 1 de len  
        self.len -= 1
        # y devolver el valor borrado
        return dato

    def __iter__(self):
        " Devuelve el iterador de la lista. "
        return _IteradorListaEnlazada(self.prim)

class _IteradorListaEnlazada(object):
    " Iterador para la clase ListaEnlazada "
    def __init__(self, prim):
        """ Constructor del iterador.  
            prim es el primer elemento de la lista. """
        self.actual = prim

    def next(self):
        """ Devuelve uno a uno los elementos de la lista. """
        if self.actual == None:
            raise StopIteration("No hay más elementos en la lista")
        
        # Guarda el dato
        dato = self.actual.dato
        # Avanza en la lista
        self.actual = self.actual.prox
        # Devuelve el dato
        return dato

