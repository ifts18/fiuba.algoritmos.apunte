
def fib(n):
	""" Precondición: n debe ser >= 0.
	    Devuelve: el número de fibonacci número n. """
	if n == 0 or n == 1:
		return n

	ant2 = 0
	ant1 = 1
	for i in xrange(2, n+1):
		fibn = ant1 + ant2
		ant2 = ant1
		ant1 = fibn
	return fibn
