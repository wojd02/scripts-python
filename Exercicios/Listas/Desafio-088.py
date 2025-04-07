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
    if decisao == 'N':
        break
for s in alunos: #sistema media
    for n in s:
        media = (s[1] + s[2]) / 2
    print(media)

print('No. NOME MÉDIA')
print('-' * 20)
for ind, aluno in enumerate(0, len(alunos)):
    print(f'{ind} {alunos[aluno][0]} {media}')

