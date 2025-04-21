def metade(val = 0, form = True):
    '''
    >>> Calcula a metade de um valor<<<
    :param val: Valor que vai ser calculado a metade
    :param form: Vai deixar formatado em um tipo de moeda que pode ser alterado na função 'MOEDA'(True/False)
    '''
    res = val / 2
    if form:#Desafio-109 tornar a formatação automatica na função
        return moeda(res)
    else:
        return res
def dobro(val = 0, form = True):
    '''
    >>> Calcula o dobro de um valor<<<
    :param val: Valor que vai ser calculado o dobro
    :param form: Vai deixar formatado em um tipo de moeda que pode ser alterado na função 'MOEDA'(True/False)
    '''
    res = val * 2
    if form:#Desafio-109 tornar a formatação automatica na função
        return moeda(res)
    else:
        return res
def aumentar(val = 0, taxa = 0, form = True):
    '''
    >>> Calcula o aumento em porcentagem de um valor<<<
    :param val: Valor que vai ser calculado o aumento
    :param taxa: Porcentagem do aumento(não utilizar o %)
    :param form: Vai deixar formatado em um tipo de moeda que pode ser alterado na função 'MOEDA'(True/False)
    '''
    acr = (val * taxa) / 100
    res = val + acr
    if form:#Desafio-109 tornar a formatação automatica na função
        return moeda(res)
    else:
        return res
def diminuir(val = 0, taxa = 0, form = True):
    '''
    >>> Calcula o decréscimo em porcentagem de um valor<<<
    :param val: Valor que vai ser calculado o decréscimo
    :param taxa: Porcentagem do decréscimo(não utilizar o %)
    :param form: Vai deixar formatado em um tipo de moeda que pode ser alterado na função 'MOEDA'(True/False)
    '''
    decr = (val * taxa) / 100
    res = val - decr
    if form:#Desafio-109 tornar a formatação automatica na função
        return moeda(res)
    else:
        return res
#Parte do desafio-108---------------------------
def moeda(val = 0, moeda = 'R$'):
    '''
    >>> Conversão e formatação de moedas<<<
    :param val: Valor que vai ser convertido e formatado
    :param moeda: Escolhe para qual moeda o valor será convertido(utilize o símbolo da moeda)
    '''
    if moeda == 'R$':
        return f'{moeda}{val:.2f}'.replace('.', ',')
    elif moeda == '$':
        return f'{moeda}{val * 0.17:.2f}'.replace('.', ',')
    elif moeda == '£':
        return f'{moeda}{val * 0.12:.2f}'.replace('.', ',')
    elif moeda == '€':
        return f'{moeda}{val * 0.15:.2f}'.replace('.', ',')
    elif moeda == '₹':
        return f'{moeda}{val * 0.06:.2f}'.replace('.', ',')
def resumo(val=0, dcr=10, acr=10):#desafio-110
    '''
    >>>Resumo de operações de um valor(dobro, metade, aumento e desconto)<<<
    :param:val: Valor para apresentar um resumo
    :param:dcr: Decréscimo em porcentagem(sem %)
    :param:acr: Acréscimo em porcentagem(sem %)
    '''
    print('-' * 35)
    print('RESUMO DO VALOR')
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(val)}')
    print(f'Dobro do preço:  \t{dobro(val, True)}')
    print(f'Metade do preço: \t{metade(val, True)}')
    print(f'{acr}% de aumento: \t{aumentar(val, acr, True)}')
    print(f'{dcr}% de redução: \t{diminuir(val, dcr, True)}')
    print('-' * 35)