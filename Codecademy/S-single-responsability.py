#Utilizando o principio de responsabilidade única
class Cadastro():
    def __init__(self, nome = str, idade = int):
        if self.__validação_dados(nome, idade):
            self.__cadastrar(nome, idade)
            self.__validação_aceita()
        else:
            self.__erro_validação_dados()
    
    def __cadastrar(self, nome = str, idade = int):
        self.nome = nome
        self.idade = idade
    def __validação_dados(self, nome = str, idade = int):
        return isinstance(nome, str) and isinstance (idade, int)
    def __validação_aceita(self):
        print('Acessando o banco de dados...')
        print(f'Usuário {self.nome} cadastrado com sucesso!')
    def __erro_validação_dados(self):
        print('ERRO: Dados inválidos! Tente novamente.')

sistema = Cadastro('Maria', 22)
