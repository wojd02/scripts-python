class People():
    def __init__(self, nome, idade, cpf, indereço): #método contrutor
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.indereço = indereço
    def apresentation(self):
        print(f'Olá meu nome é {self.nome}, eu tenho {self.idade} anos')
        self.__cpf()
        self.__ind()
    def __cpf(self): #se tentar acessar diretamente esse método, o python vai dar erro no código
        print(f'Meu cpf é {self.cpf}')
    def __ind(self):
        print(f'Meu indereço é {self.indereço}')

a1 = People('Kara', 19, '024-250-333-02', 'av. Pinheiros. Rua 372')
a1.apresentation()