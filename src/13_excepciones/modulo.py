def modulo(vector):
    """Calcula el módulo de un vector.
       Pre: el vector es una secuencia de números.
       Post: Devuelve el módulo del vector."""
    if not vector:
        raise ValueError("El vector debe tener al menos dimensión 1")
    suma = 0
    for x in vector:
        if not isinstance(x, (int, float, complex)):
            raise TypeError("El vector debe contener valores numéricos")
        suma += x * x
    return suma ** 0.5

def pedir_vector():
    vector = []
    while True:
        x = input("Ingrese un valor del vector, * para terminar: ")
        if x == "*":
            break
        try:
            vector.append(float(x))
        except ValueError:
            print("El valor no es numérico.")
    return tuple(vector)

def main():
    vector = pedir_vector()
    try:
        m = modulo(vector)
        print("El modulo de {} es {}".format(vector, m))
    except (TypeError, ValueError) as e:
        print("Error:", e)

