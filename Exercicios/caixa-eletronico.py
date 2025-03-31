#Forma que eu fiz
print('=' * 30)
print('{:^30}'.format('BANCO BANCOS'))
print('=' * 30)
valor = int(input('Qual o valor desejado para saque: '))
cedulas_50 = valor // 50
valor = valor % 50
cedulas_20 = valor // 20
valor = valor % 20
cedulas_10 = valor // 10
valor = valor % 10
cedulas_01 = valor // 1

if cedulas_50 != 0:
    print(f'{cedulas_50} cedulas de R$50,00')
if cedulas_20 != 0:
    print(f'{cedulas_20} cedulas de R$20,00')
if cedulas_10 != 0:
    print(f'{cedulas_10} cedulas de R$10,00')
if cedulas_01 != 0:
    print(f'{cedulas_01} cedulas de R$1,00')

# Outra maneira (Resolução Curso em vídeo)
print('BANCO')
value = int(input('Qual valor para saque?: '))
total = value
total_ced = 0
ced = 50
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total > 0:
            print(f'Total de {total_ced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        if ced == 20:
            ced = 10
        if ced == 10:
            ced = 1
        if total == 0:
            break