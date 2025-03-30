valor = int(input('Qual o valor desejado para saque: '))
cedulas_50 = valor // 50
valor = valor % 50
cedulas_20 = valor // 20
valor = valor % 20
cedulas_10 = valor // 10
valor = valor % 10
cedulas_01 = valor // 1

if cedulas_50 != 0:
    print(f'{cedulas_50} cedulas de R$50')
if cedulas_20 != 0:
    print(f'{cedulas_20} cedulas de R$20')
if cedulas_10 != 0:
    print(f'{cedulas_10} cedulas de R$10')
if cedulas_01 != 0:
    print(f'{cedulas_01} cedulas de R$1')