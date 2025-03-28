#for c in range (6, 0, -1):
#    print(c)
#for c in range (0, 6, -1):
#    print(c)

#i = int(input('Inicio: '))
#f = int(input('Fim: '))
#p = int(input('Passo: '))
#for c in range (i, f, p):
#    print(c)

#Contagem regrassiva - Desafio 046=======================================
#from time import sleep
#for c in range (10, -1, -1):
#    sleep(1)
#    print(c)
#print('FOGOS!!!!')

#Pares de 1 até 50 - Desafio 047=========================================
#for c in range (2, 51, 2):
#    print('.', c, end=' ')

#Pares e multiplos de 3 de 1 até 100 - Desafio 048=======================
#soma = 0
#cont = 0
#for c in range (0, 500):
#    if c % 3 == 0 and c % 2 != 0:
#        soma += c
#        cont += 1
#print(soma)
#print(cont)

#Tabuada do número que o úsuario qusier - Desafio 049====================
#n = int(input('Digite o número que você quer ver a tabuada: '))
#f = int (input('Até qual multiplicador?: '))
#for c in range (1, f+1):
#    print('{} X {} = {}'.format(n, c, n * c))

#Somando números pares - Desafio 050===========================
#soma_pares = 0
#for nc in range (1,7):
#    n = int(input('Digite o {}.o número: '.format(nc)))
#    if n % 2 == 0:
#        soma_pares += n 
#print('A soma dos números pares é {}'.format(soma_pares))

#10 primeiros termos de uma PA - Desafio 051==================
#n1 = int(input('Digite o primeiro termo da progressão: '))
#razao = int(input('Qual vai ser a razão entre eles: '))
#for c in range (0, 10):
#    print(n1, end='..')
#    n1 += razao

#Números primos - Desafios 052=================================
#total = 0
#n = int(input('Digite um número para saber se ele é primo: '))
#for c in range (1, n+1):
#    if n % c == 0:
#        print('\033[33m', end='')
#        total += 1
#    else:
#        print('\033[31m', end='')
#    print(c, end='..')

#print('\n\033[mO número {} foi divisivel {} vezes'. format(n, total))
#if total == 2:
#    print('Por esse motivo ele é primo')
#else:
#    print('Por esse motivo ele não é primo')
    

#Palíndromo - Desafios 053=====================================
#frase = str(input('Digite uma frase para saber se ela é um #políndromo: ')).strip().lower()
#frase_nova = frase.split()
#frase_nova2 = ''.join(frase_nova)
#inverso = frase_nova2[::-1]
#print(inverso)
#if frase_nova2 == inverso:
#    print('A frase {} é um palíndromo'.format(frase))
#    print('Ela invertida fica {}'.format(inverso))
#else:
#    print('A frase {} não é um palíndromo'.format(frase))
#    print('Ela invertida fica {}'.format(inverso))

#Ler ano e ver se é de maior - Desafio 054=====================
#cont_maior = 0
#cont_menor = 0
#for c in range (1,8):
#    ano_nascimento = int(input('Ano de nascimento da {}.a pessoa: ').format(c))
#    maioridade = 2025 - ano_nascimento
#    if maioridade >= 18:
#        cont_maior = cont_maior + 1
#    elif maioridade < 18:
#        cont_menor = cont_menor + 1
#print('Das sete pessoas apresentadas, {} são de maiores e {} são de menores!'.format(cont_maior, cont_menor))

#disputa peso - Desafio 055====================================
#pesado = 0
#leve = 0
#for c in range (1,6):
#    peso = (float(input('Qual o peso da pessoa?: ')))
#    if c == 1:
#       pesado = peso
#       leve = peso
#    if peso > pesado:
#        pesado = peso
#    if peso < leve:
#       leve = peso
#print('O maior peso foi de {} e o menor peso foi de'.format(pesado, leve))

#seletor pessoas - Desafio 056=================================
#nome_velho = 'a'
#velho = 0
#soma_idade = 0
#soma_mulher = 0
#for c in range (1,5):
#    nome = str(input('Qual o nome?: '))
#    idade = int(input('Qual a idade: '))
#    soma_idade = soma_idade + idade
#    if idade > velho:
#        velho = idade
#        nome_velho = nome
#    sexo = str(input('Qual sexo [M/F]: ')).upper()
#    if idade < 20 and sexo == 'F':
#        soma_mulher = soma_mulher + 1

#print('A média das idades ficou {}'.format(soma_idade/4))
#print('A pessoa mais velha é {} com a idade de {}'.format(nome_velho, velho))
#print('Tem {} mulheres com menos de 20 anos'.format(soma_mulher))


