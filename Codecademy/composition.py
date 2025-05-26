class Select:
    def by_id(self):
        print('Selecionando um elemento...')

class Insert:
    def Insert_value(self):
        print('Inserindo um valor no DB')

class Repositorio:
    def __init__(self):
        self.__select = Select() #composição
        self.__insert = Insert()
    def select_by_id(self, id: int):
        self.__select.by_id()

reposi = Repositorio()
reposi.select_by_id(13)