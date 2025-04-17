cores = [
    '\033[m',     #0 - sem cor
    '\033[1;41m', #1 - verm
    '\033[1;107m',#2 - branc
    '\033[1;30m', #3 - preto
    '\033[1;42m', # 4 - verd
]


def ajuda(comando, cor=0):
    titulo(f'Acessando o manual do comando {comando}', 4)
    print(cores[cor], end=' ')
    help(comando)
    print(cores[0], end='')


def titulo(msg, cor=0):
    print(f'{cores[cor]}', end='')
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))
    print(f'{cores[0]}', end='')


while True:
    titulo('Sistema de ajuda PyHELP', 4)
    fob = str(input('Ajuda com qual biblioteca ou função?: '))
    if fob.upper() == 'FIM':
        break
    else:
        ajuda(fob, 2)