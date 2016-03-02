from Punto import Punto

class Rectangulo:
    """Representa un rectángulo en el plano.

       Atributos:
        origen (Punto) posición de la esquina inferior izquierda.
        base (número): longitud de su base,
        altura (número): longitud de su altura,
    """
    def __init__(self, origen, base, altura):
        self.origen = origen
        self.base = base
        self.altura = altura

    def trasladar(self, dx, dy):
        self.origen = self.origen + Punto(dx,dy)

    def area(self):
        return self.base * self.altura

    def __str__(self):
        return "Origen: {}, Base: {}, Altura: {} ".format(
            str(self.origen), self.base, self.altura
        )

