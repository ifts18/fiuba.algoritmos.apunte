
def factorial(n):
    """ Precondición: n entero >=0
        Devuelve: n! """
    if n == 0:
        resultado = 1
        return resultado

    fact_ant = factorial(n-1)
    resultado = n * fact_ant
    return resultado
