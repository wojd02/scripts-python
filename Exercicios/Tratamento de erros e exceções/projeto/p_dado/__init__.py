def leiaInt(msg):
    '''
    >>>A função funciona como um input que verifica e converte o valor digitado em um valor INTEIRO<<<
    :param msg: A mensagem que o usuário vai visualizar no terminal.
    '''
    while True:
        try:
            n = int(input(f'{msg}: '))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! Número inválido, tente digitar um número inteiro!\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[0;31Entrada de dados interrompida pelo usúario\033[m')
            return 0
        else:
            return n
def leiaFloat(msg):
    '''
    >>>A função funciona como um input que verifica e converte o valor digitado em um valor REAL<<<
    :param msg: A mensagem que o usuário vai visualizar no terminal.
    '''
    while True:
        try:
            n = float(input(f'{msg}: '))
        except:
            print('\033[0;31ERRO! Número inválido, tente digitar um número real!\033[m')
        else:
            return n