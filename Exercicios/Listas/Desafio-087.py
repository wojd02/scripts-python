from random import randint
from time import sleep
sorteio = []
grupo = []
nmax = int(input('Quantos jogos você quer?: '))
for g in range (0, nmax):
    for l in range (0, 6):
        n = randint(1, 60)
        while n in grupo:
            n = randint(1, 60) 
        grupo.append(n)
    grupo.sort()
    sorteio.append(grupo[:])
    grupo.clear()

print(f'-=' * 3, ' Sorteando os jogos! ', '=-' * 3)
for c in sorteio:
    print(f'{c}')
    sleep(1)
print('-=' *3, '     BOA SORTE!      ', '=-' *3)