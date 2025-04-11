jogo = dict()
gols = list()
jogadores = list()
while True:
    jogo['nome'] = str(input('Nome do jogador: '))
    count = int(input(f'Quantas partidas {jogo["nome"]} jogou?: '))
    for p in range (1, count + 1):
        gols.append(int(input(f'Quantos gols na {p} partida: ')))
    jogo['goals'] = gols[:]
    jogo['total'] = sum(jogo['goals'])
    jogadores.append(jogo.copy())
    jogo.clear()
    gols.clear()
    decisao = str(input('Gostaria de continuar [S/N]?: ')).upper()
    while decisao not in 'SN':
        print('Decisão inválida, tente novamente!')
        decisao = str(input('Gostaria de continuar [S/N]?: ')).upper()
    if decisao == 'N':
         break
print('-'*30)
print(f'cod {'nome':>5} {"gols":>12} {"total":>13}')
for i, c in enumerate(jogadores):
    print(f'{i} {c["nome"]:>5} {c["goals"]} {c["total"]:>13}')
print('-' *30)
while True:
    decisao_jogador = int(input('Mostrar dados completos de qual jogador(999 para cancelar)?: '))
    if decisao_jogador == 999:
        print('Finalizando o programa...')
        break
    elif decisao_jogador in range(0, len(jogadores)):    
        print(f'DADOS INDIVIDUAIS DO JOGADOR {jogadores[decisao_jogador]["nome"]}')
        for i, v in enumerate(jogadores[decisao_jogador]["goals"]):
            print(f'No jogo {i+1} fez {v} gols')
    elif decisao_jogador not in range(len(jogadores)):
        print('Decisão inválida, tente novamente!')
        decisao_jogador = int(input('Mostrar dados completos de qual jogador(999 para cancelar)?: '))