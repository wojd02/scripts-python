from time import sleep
alunos = []
juncao = []
while True:
    nome = str(input('Nome: '))
    juncao.append(nome)
    n1 = float(input('Nota 1: '))
    juncao.append(n1)
    n2 = float(input('Nota 2: '))
    juncao.append(n2)
    alunos.append(juncao[:])
    juncao.clear()
    decisao = str(input('Gostaria de continuar [S/N]?: ')).upper()
    while decisao not in 'SN':
        print('Decisão inválida, tente novamente')
        decisao = str(input('Gostaria de continuar [S/N]?: ')).upper()
    if decisao == 'N':
        break
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}') #sistema layout
print('-' * 26)
for ind, aluno in enumerate (alunos):
    print(f'{ind:<4}{aluno[0]:<10}{(aluno[1] + aluno[2]) / 2:>8.1f}')
while True:
    aluno_sep = int(input('Digite o número do aluno para ver as notas separadas (999 termina): '))
    while aluno_sep not in range(0, len(alunos)): #Digitar número errado
        print('Opção inválida, tente novamente!')
        aluno_sep = int(input('Digite o número do aluno para ver as notas separadas (999 termina): '))
    if aluno_sep != 999: #busca médias separadas
        print(f'As notas do aluno(a) {alunos[aluno_sep][0]} são {alunos[aluno_sep][1]} e {alunos[aluno_sep][2]}')
    if aluno_sep == 999: #Fim programa
        print('Finalizando o programa...')
        sleep(1)
        break
