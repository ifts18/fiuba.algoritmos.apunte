#! /usr/bin/env python
# encoding: utf-8

def devuelve(valor):
	cuadrado = valor * valor
	return cuadrado

def recibe(valor):
	cuad = devuelve(valor+1)
	print cuad

recibe(5)

