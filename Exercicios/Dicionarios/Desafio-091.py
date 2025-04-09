from random import randint
from time import sleep
seletor = dict()
game = list()
ranking = list()
vencedor = list()
for p in range(1,5): # cadastro pessoas e rolagem de dados
    seletor['nome'] = str(input(f'Digite o nome do {p}.o jogador: '))
    seletor['dado'] = randint(1,6)
    game.append(seletor.copy())
    print('JOGANDO OS DADOS...')
    sleep(1)
    print(f'{seletor['nome']} tirou {seletor['dado']} no dado')
    print('-'*45)
print(f'{'-=' * 9} {"GANHADORES":^5} {'=-' * 9}')
for c in game: # colher dados e colocar em ordem em uma lista
    ranking.append(c['dado'])
ranking.sort()
for cont in game: # apresentando os vencedores
    if cont['dado'] == ranking[-1]:
        print(f'O vencedor é {cont["nome"]} com o dado no valor de {cont["dado"]}')
print(f'{'-=' * 9}{'.' *11:^5} {'=-' *9}')


