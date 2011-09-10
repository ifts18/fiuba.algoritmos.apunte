#ARCHIVO: busb.py

# condicion: es muy importante que la lista este ordenada,
# si no lo esta, este programa no funciona

# si x esta en xs devuelve xs.index(x)
# de lo contrario devuelve -1
# es decir:

# la funcion de busqueda de un elemento x
# en una lista xs ordenada


# Estrategia:
# Tomamos como intervalo inicial la lista completa: [0, len(xs)-1],
# Llamamos izq al extremo izquierdo del intervalo y
# der al extremo derecho del intervalo.
# Dado que la lista esta ordenada, sabemos que el elemento
# del medio (aquel cuyo indice med es (izq+der)//2) es mayor o igual que
# todos los elementos con indice menor,
# y menor o igual que todos los elementos con indice mayor.
# Si el elemento del medio es mayor que x, consideramos como intervalo
# busqueda al intervalo [izq, med-1] y volvemos a aplicar la misma
# estrategia para el nuevo intervalo.
# Si el elemento del medio es menor que x, consideramos como intervalo
# busqueda al intervalo [med+1, der] y volvemos a aplicar la misma
# estrategia para el nuevo intervalo.
# Si el elemento del medio es igual a x,  encontramos la solucion
# buscada, y el indice es med.

# Atencion: seguimos iterando solamente mientras el intervalo [izq, der]
# es no vacio (o sea mientras izq <= der)

def busb1(xs, x):
    izq = 0
    der = len(xs)-1
    n=len(xs)
    while izq < der: 
        med = (izq+der)//2
        if xs[med] < x: izq = med + 1 
        else: der = med

    if (izq < n):
	if (xs[izq] == x):
        	return izq
    return -1

    
    
       

