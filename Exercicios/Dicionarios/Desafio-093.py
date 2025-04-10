jogo = dict()
gols = list()
jogo['nome'] = str(input('Nome do jogador: '))
count = int(input(f'Quantas partidas {jogo["nome"]} jogou?: '))
for p in range (1, count + 1):
    gols.append(int(input(f'Quantos gols na {p} partida: ')))
jogo['goals'] = gols
jogo['total'] = sum(jogo['goals'])
print('-=' * 30)
print(jogo)
print('-=' * 30)
for c in jogo:
    print(f'O campo {c} tem o valor {jogo[c]}')
print('-=' * 30)
print(f'O jogador {jogo["nome"]} jogou {count} partidas: ')
for i, c in enumerate(jogo['goals']):
        print(f' => No jogo {i + 1}, fez {c} gols')
print(f'Foi um total de {jogo["total"]} gols!')