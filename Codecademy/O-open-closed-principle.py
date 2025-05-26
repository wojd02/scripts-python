#Utilizando o principio de aberto-fechado
class Artista:
    def __init__(self, tipo):
        self.tipo = tipo
    def apresentar_show(self):
        print(f'O(a) {self.tipo} esta apresentando seu show!')

class Palco:
    def show(self, artista = Artista):
        print('O show já vai começar!')
        artista.apresentar_show()
        print('O show acabou!')

rock_in_rio = Palco()
atração_1 = Artista('Guitarrista')
atração_2 = Artista('Lady Gaga')
rock_in_rio.show(atração_2)
