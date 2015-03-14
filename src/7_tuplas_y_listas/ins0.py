#!/usr/bin/env python
# encoding: utf-8
""" Módulo para inscribir alumnos al curso - versión 0 """

# Iniciamos la interacción con el usuario
print "Inscripcion en el curso 04 de 75.40"

# Leemos el primer padrón
padron=input("Ingresa un padrón (<=0 para terminar): ")

# Procesamos los padrones
# Inicialmente no hay inscriptos
ins = []
while padron > 0:
       # Agregamos el padrón leído a la lista de inscriptos
       ins.append(padron)

       # Leemos otro padrón más
       padron=input("Ingresá un padrón (<=0 para terminar): ")

# Mostramos el resultado       
print "Esta es la lista de inscriptos: ", ins
