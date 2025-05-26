from elemento import Elemento
from interface import Interface
class Principal(Interface):
    def __init__(self, elem: Interface):
        self.__elem = elem
    def run(self):
        self.__elem.executar()
        self.__elem()

Elemento1 = Elemento()
v = Principal(Elemento1)
v.run()