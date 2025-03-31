from random import randint
from time import sleep
cont = 0

while True:
    print('-=-' *20)
    print('Vamos jogar par ou ímpar!')
    print('-=-' *20)
    decisao_pc = randint(0, 10)
    decisao_player = int(input('Digite um número [0, 10]: '))
    decisao_time = str(input('Você quer par ou ímpar [P/I]?: ')).upper()
    soma = decisao_pc + decisao_player
    print('1.. 2.. JOGAR!')
    sleep(1)
    print(f'Eu joguei {decisao_pc} e você jogou {decisao_player} e isso fica {soma} que é', end=' ')
    print('PAR' if soma % 2 == 0  else 'ÍMPAR')
    if soma % 2 == 0:
        if decisao_time == 'P':
            print('VOCÊ GANHOU!!')
            cont += 1
        elif decisao_time == 'I':
            print('VOCÊ PERDEU!!')
            print('-=-' *20)
            break
    if soma % 2 != 0:
        if decisao_time == 'I':
            print('VOCÊ GANHOU!!')
            cont += 1
        elif decisao_time == 'P':
            print('VOCÊ PERDEU!!')
            print('-=-' *20)
            break
print(f'Você ganhou {cont} vezes!')

