#Jogo adivinhação
#import random
#nc = random.randint(1,5)
#n = int(input('Adivinhe em qual número estou pensando (1 até 5): '))
#if n == nc:
#    print('CERTO! Você acertou o número que eu estava pensando era {}, como você fez isso?'.format(nc))
#else:
#    print('NAH, você errou o número, eu estava pensando no {}'.format(nc))

#Multa
#vel = float(input('Qual a velocidade do carro (km/h)?: '))
#valor_pago = (vel - 80) * 7
#if vel>= 80:
#    print('MULTADO! Você excedeu o limite de velocidade da pista e você tem o valor de R${:.2f} em multa'.format(valor_pago))
#else:
#    print('LIBERADO, Você se manteve dentro dos limites da pista!')

#Ímpar ou par
#n = int(input('Digite um número para saber se ele é ímpar ou par: '))
#if n % 2 == 0:
#    print('O número é PAR')
#else:
#    print('O número é Ímpar')

#Preço passagem
#passagem = int(input('Quantos km/h vai ser sua viagem?: '))
#if passagem <= 200:
#    print('O valor da passagem fica R${:.2f}'.format(passagem*0.50))
#else:
#    print('O valor da passagem fica R${:.2f}'.format(passagem*0.45))

#Ano bissexto
#ano = int(input('Digite o ano que você quer saber se é bissexto: '))
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#    print('{} NÃO é bissexto'.format(ano))
#else:
#    print('{} É bissexto'.format(ano))

#Menor e maior
#n1 = int(input('Digite o primeiro número: '))
#n2 = int(input('Digite o segundo número: '))
#n3 = int(input('Digite o terceiro número: '))
#if n1 < n2 and n1 < n3:
#    print('O menor número digitado foi {}'.format(n1))
#else:
#    if n2 < n1 and n2 < n3:
#        print('O menor número digitado foi {}'.format(n2))
#    else:
#        print('O menor número digitado foi {}'.format(n3))
#if n1 > n2 and n1 > n3:
#    print('O maior número digitado foi {}'.format(n1))
#else:
#    if n2 > n1 and n2 > n3:
#        print('O maior número digitado foi {}'.format(n2))
#    else:
#        print('O menor número digitado foi {}'.format(n3))

#Ajuste salarial
#sal = float(input('Qual o valor do sálario a ser reajustado: '))
#if sal <= 1250.00:
#    print('O sálario reajustado fica R${:.2f}'.format(1250 + ((sal*15)/100)))
#else:
#    print('O sálario reajustado fica R${:.2f}'.format(1250 + ((sal*10)/100)))

#n1 = int(input('Digite a primeira reta do triangulo: '))
#n2 = int(input('Digite o segunda reta do triangulo: '))
#n3 = int(input('Digite o terceira reta do triangulo: '))
#if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
#    print('As retas podem formar um triângulo')
#else:
#    print('As retas não podem formar um triangulo')