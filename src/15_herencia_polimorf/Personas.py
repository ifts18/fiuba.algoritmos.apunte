class Persona:
    "Clase que representa a una persona."
    def __init__(self, identificacion, nombre, apellido):
        "Constructor de Persona"
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        "Devuelve una cadena representativa de la persona"
        return "%s: %s, %s" % \
            (str(self.identificacion), self.apellido, self.nombre)

class AlumnoFIUBA(Persona):
    "Clase que representa a un alumno de FIUBA."
    def __init__(self, identificacion, nombre, apellido, padron):
        "Constructor de AlumnoFIUBA"
        # llamamos al constructor de Persona
        Persona.__init__(self, identificacion, nombre, apellido)
        # agregamos el nuevo atributo
        self.padron = padron

    def __str__(self):
        "Devuelve una cadena representativa del alumno"
        return "%s: %s, %s" % \
            (str(self.padron), self.apellido, self.nombre)

