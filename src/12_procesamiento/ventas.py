# encoding: utf-8
import csv

def leer_datos(datos):
	""" Devuelve el siguiente registro o None si no hay más """
	try:
		return datos.next()
	except:
		return None

def ventas_clientes_mes(archivo_ventas):
	""" Recorre un archivo csv, con la información almacenada en el
	formato: cliente,año,mes,día,venta """

	# Inicialización
	ventas = open(archivo_ventas)
	ventas_csv = csv.reader(ventas)

	item = leer_datos(ventas_csv)
	total = 0

	while item:
		# Inicialización para el bucle de cliente
		cliente = item[0]
		total_cliente = 0
		print "Cliente %s" % cliente

		while item and item[0] == cliente:
			# Inicialización para el bucle de año
			anyo = item[1]
			total_anyo = 0
			print "\tAño: %s" % anyo

			while item and item[0] == cliente and item[1] == anyo:
				mes, monto = item[2], float(item[3])
				print "\t\tVentas del mes %s: %.2f" % (mes, monto)
				total_anyo += monto
				# Siguiente registro
				item = leer_datos(ventas_csv)

			# Final del bucle de año
			print "\tTotal para el año %s: %.2f" % (anyo, total_anyo)
			total_cliente += total_anyo

		# Final del bucle de cliente
		print "Total para el cliente %s: %.2f\n" % (cliente, total_cliente)
		total += total_cliente

	# Final del bucle principal
	print "Total general: %.2f" % total

	# Cierre del archivo
	ventas.close()

ventas_clientes_mes("ventas.csv")
