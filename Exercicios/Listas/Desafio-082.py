valores = []
pares = []
impares = []
while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 != 0:
        impares.append(n)
    decisao = str(input('Você gostaria de continuar[S/N]?: ')).upper()
    while decisao not in 'SN':
        print('Decisão inválida, tente novamente!')
        decisao = str(input('Você gostaria de continuar[S/N]?: ')).upper()
    if decisao == 'N':
        break
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
