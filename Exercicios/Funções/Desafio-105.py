boletim_final = list()
soma = soma_notas = 0
ins_boletim = dict()
ins_nota = list()
maiores = list()
soma_nomes = list()
while True:
    ins_boletim['nome'] = str(input('Nome aluno: '))
    soma_nomes = ins_boletim.copy()
    ins_nota.append(float(input('Nota: ')))
    decisao = str(input('Gostaria de adicionar outra nota[S/N]?: ')).upper()
    while decisao not in 'SN': #sistema repetição decisao continuar ou não
        print('Decisão inválida, tente novamente!')
        decisao = str(input('Gostaria de adicionar outra nota[S/N]?: ')).upper()
    while decisao == 'S': # vai ficar pedindo notas
        ins_nota.append(float(input('Nota: ')))
        decisao = str(input('Gostaria de adicionar outra nota[S/N]?: ')).upper()
        if decisao == 'N':
            break
    if decisao == 'N': #nota solo
        soma_notas = sum(ins_nota) / len(ins_nota)
        soma += len(ins_nota) # quantidade notas
        ins_boletim['notas'] = ins_nota[:]
        boletim_final.append(ins_boletim.copy())
    outro_aluno = str(input('Gostaria de adicionar outro aluno?: ')).upper() # cadastro outro aluno
    while outro_aluno not in 'SN': # validação outro_aluno
        print('Resposta inválida, tente novamente!')
        outro_aluno = str(input('Gostaria de adicionar outro aluno?: ')).upper()
    if outro_aluno == 'S': #vai limpar a lista de notas caso comece cadastro outro aluno
        ins_nota.clear()
        ins_boletim.clear()
    if outro_aluno == 'N':
        ins_nota.clear()
        ins_boletim.clear()
        break
#print(soma)
for c in boletim_final: #Maior nota
    maiores.append(max(c['notas']))
print(f'A maior nota foi {max(maiores)}')
for c in boletim_final: #menor nota
    maiores.append(min(c['notas']))
print(f'A menor nota foi {min(maiores)}')
print(f'A média da turma foi {soma_notas / len(soma_nomes)}') #media turma
if (soma_notas / len(soma_nomes)) > 7:
    print('A média da turma está ÓTIMA!')
elif 5 <= (soma_notas / len(soma_nomes)) < 7:
    print('A média da turma está OK')
elif (soma_notas / len(soma_nomes)) <= 4:
    print('A média da turma está RUIM')
    
