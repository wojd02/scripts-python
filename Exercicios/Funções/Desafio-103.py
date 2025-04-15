def ficha(nome, gols = ''):
    n_gols.isalpha()
    if len(nome) == 0:
        nome = '<Desconhecido>'
    if gols == 0 or gols.isalpha() == True or len(gols) == 0:
        gols = 0 
    print('-'* 30)
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')
jogador = str(input('Digite o nome do jogador: '))
n_gols = str(input('Número de gols: '))
ficha(jogador, n_gols)