#Injeção de dependencia
class Phone:
    def __init__(self, model = str):
        self.model = model
    def send_message(self, msg = str):
        self.msg = msg
        print(f'Sending message: {self.msg}')
    def access_site(self, site):
        self.site = site
        print(f'Accessing {self.site}')

class People:
    def __init__(self, phone = Phone):
        self.__phone = phone #Quando for utilizar uma classe em outra, mantenha a classe utilizada como privada
    def ordering_pizza(self, flavor = str):
        self.flavor = flavor
        print('Thinking about which flavor to order... OH!')
        self.__phone.send_message(f'I want a {self.flavor.upper()} pizza, please!')
        print(f'Waiting for order...')
    def study(self, subject = str):
        self.subject = subject
        print('Sitting on the chair')
        self.__phone.access_site('YouTube')
        print(f'serching class about {self.subject.upper()}')
        print('Writting down the subject')

celular = Phone('samsung')
Carla = People(celular)
Carla.ordering_pizza('pepperoni')

print()

celular_2 = Phone('iphone')
Maria = People(celular_2)
Maria.study('Math')