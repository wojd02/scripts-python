from Utilidades import moeda
n = float(input('Digite o preçoR$: '))
print(f'A metade de {moeda.moeda(n, 'R$')} é {moeda.metade(n, True)}')
print(f'O dobro de {moeda.moeda(n, 'R$')} é {moeda.dobro(n, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(n, 10, True)}')
print(f'Diminuindo 15%, temos {moeda.diminuir(n, 15, True)}')
help(moeda.moeda)