#! /usr/bin/env python
# encoding: utf-8

from Punto import Punto

class Rectangulo(object):
    """ Esta clase modela un rectángulo en el plano. """

    def __init__(self, base, altura, origen):
        """ base (número) es la longitud de su base,
            altura (número) es la longitud de su base,
            origen (Punto) es el punto del plano de su esquina
                           inferior izquierda. """
        self.base = base
        self.altura = altura
        self.origen = origen

    def trasladar(self, dx = 0, dy = 0):
        self.origen = self.origen + Punto(dx,dy)

    def area(self):
        return self.base * self.altura

    def __str__(self):
        """ muestra el rectángulo """
        return "Base: %s, Altura: %s, Esquina inf. izq.: %s " % \
               (self.base, self.altura, self.origen)

