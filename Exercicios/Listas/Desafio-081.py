valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    decisao = str(input('Gostaria de continuar [S/N]: ')).upper()
    while decisao not in 'SN':
        print('Resposta inválida, tente novamente!')
        decisao = str(input('Gostaria de continuar [S/N]: ')).upper()
    if decisao == 'N':
        break
valores.sort(reverse=True)
print(f'Você digitou {len(valores)} elementos.')
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
elif 5 not in valores:
    print('O valor 5 não faz parte da lista!')