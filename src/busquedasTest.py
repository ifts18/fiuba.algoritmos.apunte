
import bus
import busb
import busb1
import busl
import busConIndex

import random
from string import letters

import  unittest

n=1000 #cantidad de elementos de las listas usadas para testear

#funciones de busquedas a testear:
#todas deben recibir dos parametros, el primero la lista y el segundo el elemento a buscar
funciones=(bus.bus, busb.busb, busb1.busb1, busConIndex.busConIndex, busl.busl)

class testBus(unittest.TestCase):
    """ Casos de pruebas para funciones de busqueda """

    def testResultadosConocidos(self):
        """ Verifica que devuelva el indice correcto, con indices conocidos """
        xs=range(n)
        for fun in funciones:
            for i in xs:
                res=fun(xs, i)
                self.assertEqual(res, i)

    def testNoEncontrado(self):
        """ Si no se encuentra el elemento buscado debe devolver -1 """
        xs=range(n)
        for fun in funciones:
            res=fun(xs, -n)
            self.assertEqual(res, -1)

    def testListaVacia(self):
        """ Si la lista que recibe es vacia debe devolver -1 """
        xs=[]
        for fun in funciones:
            res=fun(xs, n)
            self.assertEqual(res, -1)

class consistenciaBusquedas(unittest.TestCase):
    """ Verifica que las busquedas que no necesitan que la lista este ordenada devuelvan lo mismo """

    def testConsistenciaChar(self):
        """ Consistencia de resultados entre bus, busl y busConIndex con chars """
        random.seed(14)
        xs=[random.choice(letters) for x in range(n)]
        for i in range(n):
            x=random.choice(letters)
            resb=bus.bus(xs, x)
            resbl=busl.busl(xs, x)
            resbi=busConIndex.busConIndex(xs, x)
            self.assertEqual(resb, resbi)
            self.assertEqual(resb, resbl)

if __name__ == "__main__":
    unittest.main()
