from random import randint
numeros = list()
def sortear(n):
    for p in range(0,5):
        number = randint(1, 10)
        n.append(number)
    print(n)
def soma_par(s):
    soma = 0
    for c in s:
        if c % 2 == 0:
            soma += c
    print(f'A soma entre os pares foi {soma}')
sortear(numeros)
soma_par(numeros)