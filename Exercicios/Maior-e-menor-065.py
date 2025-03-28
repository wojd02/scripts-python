soma = cont = menor = maior = 0
desejo = 's'
while desejo == 's':
    n = int(input('Digite um número: '))
    desejo = str(input('Deseja continuar[S/N]')).lower()
    soma += n
    cont += 1
    if menor == 0: menor = n
    if menor > n: menor = n
    if maior < n: maior = n

print('A média dos números foi {:.1f}'.format(soma/cont))
print('O menor número digitado foi {}'.format(menor))
print('O maior número digitado foi {}'.format(maior))