class Client:
    def __init__(self, id, adress): #Atributos (id, adress)
        self.id = id
        self.adress = adress
    def adress_catcher(name): #Método
        print(name.adress)
    def say_id():
        print('My id is {self.id}')
        
#Criando uma instância
Kara = Client(1, 'Rua Alameda ANT, n198')
print(Kara.id) #O output desse comando é um atributo (1)
print(Kara.adress) #O output desse comando é um atributo ('Rua Alameda ANT, n198')

Client.adress_catcher(Kara) #Utilizando um método da classe Client


#Criando uma sub-classe
#class Animal:
#    def __init__(self, name):
#        self.name = name
#    def make_noise(self):
#        print('grrrr')

#class cat(Animal):
#    def make_noise(self):
#        print('Meow')

#pet1 = Animal('Tec')
#pet1.make_noise()
#pet2 = cat('Maisy')
#pet2.make_noise()