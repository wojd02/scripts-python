from projeto import p_interface
from projeto import arquivo
from projeto import p_dado
from time import sleep

arq = 'pessoas.txt' #Validar se arquivo existe
if arquivo.ExistArq(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não foi encontrado')

if not arquivo.ExistArq(arq): #Criar arquivo
    arquivo.CriarArq(arq)

while True:
    opção = (p_interface.menu(['ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema']))
    if opção == 1:
        arquivo.LerArq(arq)
    elif opção == 2:
        print('-' * 45)
        print(f'{'NOVO CADASTRO':^45}')
        print('-' * 45)
        nome = str(input('Nome: '))
        idade = p_dado.leiaInt('Idade')
        arquivo.cadastrar(arq, nome, idade)
    elif opção == 3:
        print('ENCERRANDO O PROGRAMA...')
        sleep(1)
        break
    else:
        print('\033[0;31mERRO! Opção inválida, tente novamente!\033[m')