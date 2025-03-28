#Analisador-valores - Desafio 066======================================
#soma = cont = 0
#while True:
#    n = int(input('Digite um número (999 para parar): '))
#    if n == 999:
#        break
#    soma += n
#    cont += 1
#print(f'A soma dos valores digitados foi de {soma}')
#print(f'Foram digitados {cont} valores na lista')

#Tabuada - Desafio 067=================================================
while True:
    cont = 1
    print('-=-' * 15)
    n = int(input('Quer ver a tabuada de qual número?: '))
    print('-=-' * 15)
    if n > 0:
        while cont <= 10:
            print(f'{n} X {cont} = {n*cont}')
            cont += 1
    elif n < 0:
        print(f'Fim do programa!')
        break

#