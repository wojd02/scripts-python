import moedas2
n = float(input('Digite o preçoR$: '))
print(f'A metade de {moedas2.moeda(n, 'R$')} é {moedas2.moeda(moedas2.metade(n))}')
print(f'O dobro de {moedas2.moeda(n, 'R$')} é {moedas2.moeda(moedas2.dobro(n))}')
print(f'Aumentando 10%, temos {moedas2.moeda(moedas2.aumentar(n, 10))}')
print(f'Diminuindo 15%, temos {moedas2.moeda(moedas2.diminuir(n, 15))}')