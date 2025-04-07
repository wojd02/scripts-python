matriz = [[], [], []]
somapar = soma3 = 0
for c in range(0,3):
    for l in range (0,3):
        matriz[c].append(int(input(f'Digite o valor da casa [{c}, {l}]')))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[c][l] % 2 == 0:
            somapar += matriz[c][l]
        if l == 2:
            soma3 += matriz[c][l]
    print('')
print(f'A soma dos pares na matriz é {somapar}')
print(f'A soma da terceira linha é {soma3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')

