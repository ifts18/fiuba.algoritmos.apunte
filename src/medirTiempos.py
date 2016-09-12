
""" Este modulo permite medir el tiempo que demora la ejecucion de una funcion
Utiliza el modulo de python timeit """

import  timeit

n=100000 #cantidad de veces que se ejecuta la funcion a medir


def medir_tiempos(fun, lista_parametros, *archivo):
	"""Esta funcion permite medir el tiempo que demora la ejecucion de otra
	funcion que recibe como parametro.
	Devuelve un float que representa el tiempo en segundos que demoro
	ejecutar n veces la funcion medida.
	Pre:
		fun		:Cadena de caracteres con el nombre de la
				funcion a medir. No debe prefijarse con el
				nombre del modulo de la cual se importa

		lista_parametros:lista con los parametros a pasarle a la
				funcion a medir.

		archivo		:parametro opcional, cadena de caracteres con
				el nombre del archivo donde se encuentra la
				funcion a medir. Si se omite busca la funcion
				en el mismo archivo donde se realiza la llamada
				a medir_tiempos
	   Post:
				Devuelve un float, tiempo en segundos que
				demoro ejecutar	la funcion n veces.

	   Ejemplo 1:
		medir_tiempos("busb",[[1,2,3,4,5,6,7,8,9,10], 10],"busb.py")
		Devuelve el tiempo en segundos que demoro ejecutar n veces la
		funcion	busb([1,2,3,4,5,6,7,8,9,10], 10).
		La funcion busb, se encuentra definida en el archivo busb.py

	   Ejemplo 2:
		medir_tiempos("test",[])
		Devuelve el tiempo en segundos que demoro ejecutar n veces la
		funcion	test().
		La funcion test, se encuentra definida en el mismo archivo
		(o interprete) de donde se llamo a medir_tiempos """

	if(len(archivo)>=1):
                modulo=archivo[0][:-3] # elimina la extension del archivo .py
		sentencia_import="import "+modulo
		fun=modulo+"."+fun #prefija la funcion con el nombre del modulo
	else:
		#si se omite el archivo, importa la funcion del mismo archivo
		#desde donde se llama a medir_tiempos
		sentencia_import="from __main__ import "+fun

	parametros="("
	i=0
	while (i < len(lista_parametros)):
		parametros=parametros+repr(lista_parametros[i])+', '
		i+=1
	if (len(lista_parametros)>0): parametros=parametros[:-2]
	parametros=parametros+')'
	sentencia=fun+parametros

	t=timeit.Timer(sentencia, sentencia_import) #ver help(timeit.Timer)
	res=t.timeit(n) #ver help(timeit.Timer.timeit)
	return res

