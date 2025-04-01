#Desafio 73 - Times futebol
times = 'Fortaleza', 'Juventude', 'Vasco da gama', 'Cruzeiro', 'Grêmio', 'Bragantino', 'Ceará SC', 'Corinthians', 'Flamengo', 'Internacional', 'Bahia', 'São Paulo', 'Sport Recife', 'Botafogo', 'Palmeiras', 'Atlético-MG', 'Santos', 'Mirassol', 'Fluminense', 'EC Vitória'

print(f'Os primeiros 5 times da tabela são {times[0:5]}')
print('-=-' *35)
print(f'Os últimos 4 colocados da tabela do brasileirão são {times[16:20]}')
print('-=-' *35)
print(f'Os times em ordem alfabética: {sorted(times)}')
print('-=-' *35)
print(f'O Mirassol se encontra na {times.index('Mirassol') + 1} posição')