#Apenas resposta certa - Desafio 057=============================
#sexo = 'a'
#while sexo not in 'FM':
#    sexo = str(input('Qual o sexo dessa pessoa? [M/F]?: ')).strip().upper()[0]
#print('FIM')

#Pense de 0 a 10 até acertar - Desafio 058=======================
#from random import randint
#numero_pc = randint(1,10)
#cont = 0
#resp = 0

#while resp != numero_pc:
#    resp = int(input('Em qual número estou pensando agora?: '))
#    cont += 1
#if cont <= 3:
#    print('PARABENS, Você acertou o número em {} tentativas'.format(cont))
#elif 3 < cont <= 5:
#    print('Poderia ter sido melhor! Você precisou de {} tentativas'.format(cont))
#else:
#    print('Ruim demais, esse jogo não é seu ponto forte, você precisou de {} tentativas pra acertar'.format(cont))

# manu calculadora - Desafio 059=================================
#from os import environ
#from time import sleep
#n1 = int(input('Digite o primeiro valor: '))
#n2 = int(input('Digite o segundo valor: '))
#resp_calc = 0

#while resp_calc != 5:
#    resp_calc = int(input('-=-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-\n[1] - somar: \n[2] - multiplicar:\n[3] - maior:\n[4] - novos números:\n[5] - sair do programa:\n      Digite a opção:\n -=-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=- '))
#    if resp_calc == 1:#
#        print('A soma de {} e {} é {}'.format(n1, n2, n1+n2))
#    elif resp_calc == 2:
#        print('A multiplicação entre {} e {} é {}'.format(n1, n2, n1*n2))
#    elif resp_calc == 3:
#        if n1 > n2:
#            print('O número {} é maior que {}'.format(n1, n2))
#        else:
#            print('O número {} é maior que {}'.format(n1, n2))
#    elif resp_calc == 4:
#        n1 = int(input('Qual o novo valor: '))
#        n2 = int(input('Qual o novo valor: '))
#    elif resp_calc == 5:
#        print('SAINDO DO PROGRAMA...')
#        sleep(2)
#    else:
#       print('Opção invalida, tente novamente...')
#print('Fim do programa')

#Fatorial - Desafio 060==============================================================
#n = int(input('Digite um número para saber o fatorial: '))
#cont = 1
#n2 = n
#fat = n
#while cont < n:
#    print('{}'.format((n2 + 1) - cont), end=' ')
#    n3 = n * (n2 - cont)
#    fat = n
#    n = n3
#    cont += 1
#print('= {}'.format(fat))

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}!='.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c> 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

#P.A #2 - Desafio 061============================================
#n = int(input('Digite um número: '))
#razao = int(input('Qual a razão da PA: '))
#cont = 0

#while cont <= 10:
#    cont += 1
#    print(n, end='..')
#    soma = n + razao
#    n = soma
