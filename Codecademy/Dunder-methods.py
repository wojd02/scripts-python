class Estoque:
    def __init__(self, qtd_prod): #Dunder method __method-name__
        if not isinstance (qtd_prod, int):
            qtd_prod = int(qtd_prod)
            self.qtd_prod = qtd_prod

    def __add__(self, n):
        if  not isinstance(n, int):
            n = int(n)
            return self.qtd_prod + n


#x = Estoque(2.3)
#print(x + 3.5)

lista = ['30m', 55.000,'13mi', 230.000000, 200.000, '5bi', '230m','50']
class Conversor:
    def __init__(self, lista):
        self.list = lista
    def conversion(self):
        new_list = []
        for i in self.list:
            if isinstance(i, str):
                if 'mi' in i:
                    i = float(i.replace('mi', ''))
                    i *= 1000000
                elif 'bi' in i:
                    i = float(i.replace('bi', ''))
                    i *= 1000000000
                elif 'm' in i:
                    i = float(i.replace('m', ''))
                    i *= 1000
                else:
                    i = float(i)
                new_list.append(i)
            else:
                new_list.append(i)
        return new_list    
converted_list = Conversor(lista).conversion()
print(type(converted_list[7]))
print(lista)
print(converted_list)