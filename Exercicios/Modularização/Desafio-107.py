from Utilidades import moeda
n = float(input('Digite o preçoR$: '))
print(f'A metade de R${n} é {moeda.metade(n)}')
print(f'O dobro de R${n} é {moeda.dobro(n)}')
print(f'Aumentando 10%, temos {moeda.aumentar(n, 10)}')
print(f'Diminuindo 15%, temos {moeda.diminuir(n, 15)}')