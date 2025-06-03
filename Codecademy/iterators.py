import itertools
#num = int(input('Digite um número: '))
#for c in itertools.count(0,2):
#    print(c)
#    if c >= num:
#        break

#lista = [1,7,4,3,6]
#iter_list = lista.__iter__() #transforma o elemento na classe iterator
#list_colors = ['red', 'blue', 'purple', 'cyan', 'green', 'black', 'white', 'yellow', 'orange', 'grey']
#list_numbers = [1, 7, 3, 5, 2]
#mix_colors_3 = itertools.combinations(list_colors, 3)
#mix_numbers_2 = itertools.combinations(list_numbers, 2)
#for mix in mix_numbers_2:
#    print(mix) 

#difference between YIELD and RETURN
def teste():
    yield 'look'
    yield 'this'
    yield 'string'

def teste2():
    return 'look'
    return 'this'
    return 'string'
test = teste2()
for c in test:
    print(c)