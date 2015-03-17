#/usr/bin/env python
# encoding: utf-8

# Módulo para hacer validaciones de tipos
from validaciones import es_numero

class Punto(object):
    """ Representación de un punto en el plano, los atributos son x e y que
        representan los valores de las coordenadas cartesianas."""
    def __init__(self, x=0, y=0):
        """ Constructor de Punto, los valores de x e y deben ser numéricos,
            de no ser así, se levanta una excepción TypeError """
        if es_numero(x) and es_numero(y):
            self.x=x
            self.y=y
        else:
            raise TypeError("x e y deben ser valores numéricos")

    def restar(self, otro):
        """ Devuelve un nuevo punto, con la resta entre dos puntos. """
        return Punto(self.x - otro.x, self.y - otro.y)

    def norma(self):
        """ Devuelve la norma del vector que va desde el origen
            hasta el punto. """
        return (self.x*self.x + self.y*self.y)**0.5

    def distancia(self, otro):
        """ Devuelve la distancia entre ambos puntos. """
        r = self.restar(otro)
        return r.norma()

    def mover(self, u=0, v=0):
        """ Traslada un punto en x y/o en y. """
        self.x = self.x+u
        self.y = self.y+v

    def __str__(self):
        """ Muestra el punto como un par ordenado. """
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __add__(self, otro):
        """ Devuelve la suma de ambos puntos. """
        return Punto(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        """ Devuelve la resta de ambos puntos. """
        return Punto(self.x - otro.x, self.y - otro.y)

    def __eq__(self, otro):
        """ Devuelve si dos puntos son iguales. """
        return self.x == otro.x and self.y == otro.y

    def __ne__(self, otro):
        """ Devuelve si dos puntos son distintos. """
        return not self == otro

    def __mul__(self, escalar):
        if es_numero(escalar):
            return Punto(self.x * escalar, self.y * escalar)
        else:
            raise TypeError ("Sólo se puede multiplicar por un escalar")

    def __rmul__(self, escalar):
        return self * escalar
