#Sequencia de fibonacci============================================================================
contador = int(input('Quantas casas da sequencia você quer ver?: '))
cont = 0
n1 = 0
n2 = 1
while cont < contador:
    cont += 1
    print(n1, end='..')
    fibonacci = n1 + n2
    n1 = n2
    n2 = fibonacci