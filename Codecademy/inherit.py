class Animais:
    def __init__(self, localizaçao):
        self.localizaçao = localizaçao
    def andar(self):
        print(f'O animal esta andando por {self.localizaçao}')

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

Miauzin = Gato('Arizona')
Miauzin.miar()
print()
Mordiscado = Cachorro('Rio De Janeiro')
Mordiscado.latir()