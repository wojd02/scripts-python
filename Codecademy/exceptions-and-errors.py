
s = 0
v1 = 3
v2 = 0
try:
    s = v1 / v2
except ZeroDivisionError as erro:
    print(erro)
    print(f'Não podemos dividir {v1} por 0')
else:
    print(f'O resultado da divisão de {v1} por {v2} é {s}')
finally:
    print('Saindo do programa...')