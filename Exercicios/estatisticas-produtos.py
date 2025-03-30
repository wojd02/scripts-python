soma = cont = produto_barato = nome_produto_barato = 0
decisao = 'S'
while True:
    print('-' * 30)
    print('        SUPER-MERCADÃO')
    print('-' * 30)
    if decisao == 'S':
        nome_produto = str(input('Digite o nome do produto: ')).upper()
        preco_produto = float(input('Digite o valor do produto: '))
        decisao = str(input('Gostaria de continuar [S/N]?: ')).upper()
        while decisao not in 'SN':
            print('Decisão inválida, por favor tente novamente!')
            decisao = str(input('Gostaria de continuar [S/N]?: ')).upper()
        soma += preco_produto
        if preco_produto >= 1000:
            cont += 1
        if produto_barato == 0:
            produto_barato = preco_produto
            nome_produto_barato = nome_produto
        elif produto_barato > preco_produto:
            produto_barato = preco_produto
            nome_produto_barato = nome_produto
    else:
        print('PROGRAMA ENCERRADO')
        break
print(f'O total foi de {soma}')
print(f'O produto mais barato da lista foi {nome_produto_barato} com o valor de {produto_barato:.2f}')
print(f'{cont} produtos custaram mais que R$ 1000,00')
    

