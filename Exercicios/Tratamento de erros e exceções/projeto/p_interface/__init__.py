def menu(lista):
    '''
    >>>Faz um menu pesonalizado com uma lista<<<
    :param lista: Lista que vai mostrar as opções do menu
    '''
    from projeto import p_dado
    from time import sleep
    c = 1
    print('-' * 45)
    print(f'{'MENU PRINCIPAL':^45}')
    print('-' * 45)
    for item in lista:
        print(f'\033[0;35m{c} - {item}\033[m')
        c+=1
    print('-' * 45)
    opção = p_dado.leiaInt('\033[0;32mSua opção\033[m')
    return opção