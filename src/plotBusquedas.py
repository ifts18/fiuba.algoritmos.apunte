"""Requiere el modulo pylab
   http://matplotlib.sourceforge.net"""

from pylab import *
from medirBusquedas import *


def graficar_resultados():
    font = {'fontname': 'Courier',
            'color': 'r',
            'fontweight': 'bold',
            'fontsize': 11}
    res = medir_busquedas_exitosas(0, 100, 10)
    x = arange(0, 100, 10)
    i = 2
    for funcion in diccionario_funciones.keys():
        lista = []
        for n in sorted(res):
            lista.append(res[n][funcion])
            figure(1)
            plot(x, lista, label=funcion)
            figure(i)
            grid(True)
            title(funcion)
            plot(x, lista)
            xlabel("n", font)
            ylabel("tiempo [seg]", font)
            savefig(funcion, dpi=100)
            i += 1
        figure(1)
        grid(True)
        title("Comparacion de las funciones")
        legend()
        xlabel("n", font)
        ylabel("tiempo [seg]", font)
        savefig("Comparacion", dpi=100)

if __name__ == "__main__":
    graficar_resultados()
