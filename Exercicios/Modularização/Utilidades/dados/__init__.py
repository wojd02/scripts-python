def money(msg):
    '''
    >>>A função funciona como um input que verifica e converte o valor digitado em um valor MONETÁRIO<<<
    :param msg: A mensagem que o usuário vai visualizar no terminal.
    '''
    valor = 0
    ok = False
    while ok == False:
        n = str(input(msg)).strip()
        if n.isnumeric() == True or n.isalpha() == True or n.isalnum() == True or n.isdigit() == True or n.isspace() == True:
            print('\033[1;31mMensagem inválida, digite um valor monetário\033[m')
        else:
            valor = float(n.replace(',', '.'))
            ok = True
        if ok == True:
            break
    return valor

def leiaINT(msg):
    '''
    >>>A função funciona como um input que verifica e converte o valor digitado em um valor INTEIRO<<<
    :param msg: A mensagem que o usuário vai visualizar no terminal.
    '''
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric() == True:
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mMensagem inválida, digite um número por gentileza!\033[m')
        if ok:
            break
    return valor
