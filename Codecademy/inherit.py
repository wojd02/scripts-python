class Animais:
    def __init__(self, localizaçao):
        self.localizaçao = localizaçao
    def andar(self):
        print(f'O animal esta andando por {self.localizaçao}')
    def _dormir(self): #encapsulamento protegido, só pode ser acessado na classe e nas classes filhas
        print('O animal esta dormindo')

class Gato(Animais):
    def __init__(self, localizaçao):
        super().__init__(localizaçao)
    def miar(self):
        print('Miau')
        self.andar()
class Cachorro(Animais):
    def __init__(self, localizaçao):
        super().__init__(localizaçao)
    def latir(self):
        print('Roof')
        self.andar()
        self._dormir()

Miauzin = Gato('Arizona')
Miauzin.miar()
print()
Mordiscado = Cachorro('Rio De Janeiro')
Mordiscado.latir()
print()
Mordiscado._dormir() #Isso aqui não poderia acontecer, pois objetos não podem chamar métodos privados.