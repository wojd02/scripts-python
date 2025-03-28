#P.A #3 - Desafio 061====================================================================================================================================================
n = int(input('Digite um número: '))
razao = int(input('Qual a razão da PA: '))
cont = 0
continuacao = 'S'

while cont <= 10:
    cont += 1
    print(n, end='..')
    soma = n + razao
    n = soma

while continuacao == 'S':
    continuacao = str(input('\nQuer continuar? [S/N]: ')).upper()
    if continuacao == 'S':
        cont2 = cont
        print('-=-' *20)
        razao2 = int(input('Quantos números mais você quer:\n[1] - 5 termos\n[2] - 10 termos\n[3] - 15 termos\n[4] - 20 termos\n[5] - [0] termos\nOpção :'))
        print('-=-' *20)
        if razao2 == 1:
            while cont <= cont2 + 4:
                cont += 1
                print(n, end='..')
                soma = n + razao
                n = soma
        elif razao2 == 2:
            while cont <= cont2 + 9:
                cont += 1
                print(n, end='..')
                soma = n + razao
                n = soma
        elif razao2 == 3:
            while cont <= cont2 + 14:
                cont += 1
                print(n, end='..')
                soma = n + razao
                n = soma
        elif razao2 == 4:
            while cont <= cont2 + 19:
                cont += 1
                print(n, end='..')
                soma = n + razao
                n = soma
        elif razao2 == 5:
            print('FIM DO PROGRAMA')
    else:
        continuacao = 'N'