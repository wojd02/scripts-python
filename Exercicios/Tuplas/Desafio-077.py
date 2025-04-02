itens = 'praticar', 'ensinar', 'aprender', 'programar', 'acessar','entender', 'escutar', 'ver', 'curso', 'vizualizacao', 'encaminhar'
vogais = ['a', 'e', 'i', 'o', 'u']

for c in itens:
    print(f'\nNa palavra {c.upper()} temos: ', end=' ')
    for letra in c:
        if letra in vogais:
            print(letra, end=' ')