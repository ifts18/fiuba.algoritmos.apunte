#ARCHIVO: bus.py

# la funcion de busqueda de un elemento x
# en una lista xs

# si x esta en xs devuelve xs.index(x)
# de lo contrario devuelve -1

def bus(xs, x):

     if x in xs:
          return(xs.index(x))
     else:
          return(-1)



