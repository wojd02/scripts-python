from interface.elementoInterface import Interface
class Elemento(Interface):
    def executar(self):
        print('Executando o elemento')
class Elemento2(Interface):
    def executar(self):
        print('Executando o elemento alternativo')