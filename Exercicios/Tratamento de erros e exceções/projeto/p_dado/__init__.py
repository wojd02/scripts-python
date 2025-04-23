def leiaInt(msg):
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
    while True:
        try:
            n = float(input(f'{msg}: '))
        except:
            print('\033[0;31ERRO! Número inválido, tente digitar um número real!\033[m')
        else:
            return n