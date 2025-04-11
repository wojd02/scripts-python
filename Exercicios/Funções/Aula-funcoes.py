def traco(msg):
    print('-' *30)
    print(msg)
    print('-' * 30)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos +=1
valores = [2, 4, 6, 8, 10]
traco('Aula de funções no python!')
dobra(valores)
