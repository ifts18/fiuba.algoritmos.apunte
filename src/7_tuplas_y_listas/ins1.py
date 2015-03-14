#!/usr/bin/env python
# encoding: utf-8
""" Módulo para inscribir alumnos al curso - versión 1 """

# Iniciamos la interacción con el usuario
print "Inscripcion en el curso 04 de 75.40"

# Leemos el primer padrón
padron=input("Ingresa un padrón (<=0 para terminar): ")

# Procesamos los padrones
# Inicialmente no hay inscriptos
ins = []
while padron > 0:
       # Si todavía no está, agregamos el padrón a la lista de inscriptos,
       if padron not in ins:
              ins.append(padron)
       # de lo contrario avisamos que ya figura
       else:
              print "Ya figura en la lista"

       # Leemos otro padrón mas
       padron=input("Ingresá un padrón (<=0 para terminar): ")

# Mostramos el resultado       
print "Esta es la lista de inscriptos: ", ins
