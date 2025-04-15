def funcao(number, show = 'N'):
    """
    Calculando fatorial
    :param n: Número a ser calculado
    :param show: mostrar ou não a operação
    :return: retorna o valor do fatorial
    """
    fat = 1
    if decisao == 'S':
        for c in range(number, 0, -1):
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
            fat *= c
    elif decisao == 'N':
        for c in range(number, 0, -1):
            fat *= c
        print(f'{number}! =', end=' ')
    return fat
n = int(input('Digite um número: '))
decisao = str(input('Mostrar operação[S/N]?: ')).upper()
while decisao not in 'SN':
    print('Decisão inválida, tente novamente!')
    decisao = str(input('Mostrar operação[S/N]?: ')).upper()
print(funcao(n, decisao))