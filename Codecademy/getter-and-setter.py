class MyHouse():
    def __init__(self) -> None: # -> É o operador que especifica o tipo de retorno de uma função ou método (é usado para deixar claro que a função não retorna nenhum valor de interesse.)
        self.__color = None
        self.__number = None
    def setter_color(self, color = str):
        self.__color = color
    def setter_number(self, number = int):
        self.__number = number
    def getter_color(self):
        return self.__color
    def getter_number(self):
        return self.__number
 
minha_casa = MyHouse()
print(minha_casa.getter_number())
minha_casa.setter_number(177)
minha_casa.setter_color('red and black')
print(minha_casa.getter_number(), minha_casa.getter_color())
