listagem = 'Lápis', 1.99, 'Caneta', 2.50, 'Caderno', 10.00, 'Estojo', 7.00, 'Régua', 3.50, 'Marcador', 3.50, 'Lapiseira', 7.50, 'Tesoura', 5.00, 'Estilete', 6.00, 'Borracha', 3.35, 'Apontador', 4.50, 'Lápis de cor', 7.50
print('-=' *20)
print(f'{"LISTA DE PREÇOS:":^40}')
print('-=' *20)
for c in range (0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}', end='')
    else:
        print(f'R${listagem[c]:>7.2f}')