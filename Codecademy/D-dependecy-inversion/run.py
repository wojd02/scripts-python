from elementos.elemento import Elemento2
from interface import Interface
class Principal():
    def __init__(self, elem: Interface):
        self.__elem = elem
    def run(self):
        self.__elem.executar()
        self.__elem

Elemento1 = Elemento2()
v = Principal(Elemento1)
v.run()