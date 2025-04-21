def metade(val = 0):
    res = val / 2
    return res
def dobro(val = 0):
    res = val * 2
    return res
def aumentar(val = 0, taxa = 0):
    acr = (val * taxa) / 100
    res = val + acr
    return res
def diminuir(val = 0, taxa = 0):
    decr = (val * taxa) / 100
    res = val - decr
    return res
#Parte do desafio-108---------------------------
def moeda(val = 0, moeda = 'R$'):
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
