from projeto import p_interface
from time import sleep

while True:
    opção = (p_interface.menu(['ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema']))
    if opção == 1:
        print('opc 1')
    elif opção == 2:
        print('opc 2')
    elif opção == 3:
        print('ENCERRANDO O PROGRAMA...')
        sleep(1)
        break
    else:
        print('\033[0;31mERRO! Opção inválida, tente novamente!\033[m')