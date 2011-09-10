#! /usr/bin/env python
#encoding: latin1

#validaciones de condiciones generales de los datos
from validaciones import es_numero, es_cadena_no_vacia

class Hotel(object):
    """ Hotel: sus atributos son: nombre, ubicacion, puntaje y precio. """

    def __init__(self, nombre = '*', ubicacion = '*', 
                 puntaje = 0, precio = float("inf")):
        """ nombre y ubicacion deben ser cadenas no vacías,
            puntaje y precio son números.  
            Si el precio es 0 se reemplaza por infinito. """

        if es_cadena_no_vacia (nombre):
            self.nombre = nombre
        else:
            raise TypeError ("El nombre debe ser una cadena no vacía")

        if es_cadena_no_vacia (ubicacion):
            self.ubicacion = ubicacion
        else:
            raise TypeError ("La ubicación debe ser una cadena no vacía")

        if es_numero(puntaje):    
            self.puntaje = puntaje
        else:
            raise TypeError ("El puntaje debe ser un número")

        if es_numero(precio):
            if precio != 0:
                self.precio = precio
            else:
                self.precio = float("inf")
        else:
            raise TypeError("El precio debe ser un número")

    def __str__(self):
        """ Muestra el hotel según lo requerido. """
        return self.nombre + " de "+ self.ubicacion+ \
                " - Puntaje: " + str(self.puntaje) + " - Precio: "+ \
                str(self.precio)+ " pesos."

    def ratio(self):
        """ Calcula la relación calidad-precio de un hotel de acuerdo 
            a la fórmula que nos dio el cliente. """
        return ((self.puntaje**2)*10.)/self.precio

    def __cmp__(self, otro):
        """ Compara dos hoteles por su relación calidad-precio. """
        diferencia = self.ratio() - otro.ratio()
        if diferencia < 0:
            return -1
        elif diferencia > 0:
            return 1
        else:
            return 0

    def cmpPrecio(self, otro):
        """ Compara dos hoteles por su precio. """
        return cmp(self.precio, otro.precio)

    def cmpPuntaje(self, otro):
        """ Compara dos hoteles por su puntaje. """
        return cmp(self.puntaje, otro.puntaje)


#    def __eq__(self, p):
#        return self.ratio() == p.ratio()
#
#    def __lt__(self, p):
#        return self.ratio() < p.ratio()
#
#    def __gt__(self, p):
#        return self.ratio() > p.ratio()
#
#    def __le__(self, p):
#        return self.ratio() <= p.ratio()
#
#    def __ge__(self, p):
#        return self.ratio() >= p.ratio()
#
# el metodo que hace falta para comparar hoteles entre si
#    def compararHoteles(self, p):
#        """ya se definieron __lt__ y __eq__
#           segun la relacion calidad--precio"""
#
#        if self < p:
#            return -1
#        elif self == p:
#            return 0
#        else:
#            return 1
#

