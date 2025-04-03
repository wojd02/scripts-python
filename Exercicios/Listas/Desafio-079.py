valores = []
while True:
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
    else:
        print('Esse número já foi inserido na lista... Não será inserido a duplicata')
    decisao = str(input('Gostaria de continuar[S/N]?: ')).upper()
    while decisao not in 'SN':
        print('Opção inválida, tente novamente!')
        decisao = str(input('Gostaria de continuar[S/N]?: ')).upper()
        if decisao == 'SN':
            break
    if decisao == 'N':
        break
valores.sort()
print(valores)

    