
def fib(n):
	""" Precondición: n debe ser >= 0.
	    Devuelve: el número de fibonacci número n. """
	if n == 0 or n == 1:
		return n
	return fib(n-1) + fib(n-2)
