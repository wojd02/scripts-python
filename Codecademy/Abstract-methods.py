from abc import ABC, abstractmethod

class Pessoas(ABC):
    def alimentar(self): #Essa função é um objeto
        print('A pessoa esta se alimentando')
    
    @abstractmethod #A classe filha PRECISA criar essa função no seu escopo, pois aqui ela não é um objeto
    def trabalhar(self):
        pass

class Pro_player(Pessoas):
    def trabalhar(self):
        print('O pro player esta treinando')
class Aluno(Pessoas):
    def trabalhar(self):
        print('O aluno esta estudando')

aq1 = Pro_player()
aq2 = Aluno()
aq1.alimentar() #Esse objeto vai ser definido para todas as classes filhas de Pessoas pois não é abstrato
aq1.trabalhar() #Esse objeto PRECISA ser definido na classe filha, caso contrario vai dar erro pois ela só existe de forma abstrata
aq2.alimentar()
aq2.trabalhar()