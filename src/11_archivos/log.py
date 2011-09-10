#! /usr/bin/env python
# encoding: latin1

# El módulo datetime se utiliza para obtener la fecha y hora actual.
import datetime

def abrir_log(nombre_log):
    """ Abre el archivo de log indicado. Devuelve el archivo abierto.
    Pre: el nombre corresponde a un nombre de archivo válido.
    Post: el archivo ha sido abierto posicionándose al final. """
    archivo_log = open(nombre_log, "a")
    guardar_log(archivo_log, "Iniciando registro de errores")
    return archivo_log

def guardar_log(archivo_log, mensaje):
    """ Guarda el mensaje en el archivo de log, con la hora actual.
    Pre: el archivo de log ha sido abierto correctamente.
    Post: el mensaje ha sido escrito al final del archivo. """
    # Obtiene la hora actual en formato de texto
    hora_actual = str(datetime.datetime.now())
    # Guarda la hora actual y el mensaje de error en el archivo
    archivo_log.write(hora_actual+" "+mensaje+"\n")

def cerrar_log(archivo_log):
    """ Cierra el archivo de log.
    Pre: el archivo de log ha sido abierto correctamente.
    Post: el archivo de log se ha cerrado. """
    guardar_log(archivo_log, "Fin del registro de errores")
    archivo_log.close()
