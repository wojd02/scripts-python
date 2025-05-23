class Car:
    def __init__(self, modelo):
        self.modelo = modelo
    def ligar(self):
        print(f'A pessoa ligou o {self.modelo} e esta dirigindo')
    def desligar(self):
        print(f'A pessoa estacionou o {self.modelo} e desligou')

class People:
    def dirigir (self, carro = Car):
        carro.ligar()
    def estacionar (self, carro = Car):
        carro.desligar()
    def trancar_carro (self):
        print('A pessoa saiu e trancou o carro')

Anthony = People()
carro = Car('Celta')

Anthony.trancar_carro()
        