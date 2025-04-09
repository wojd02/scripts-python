boletim = {}
boletim['nome']= str(input('Nome: '))
boletim['média']=float(input(f'Média de {boletim["nome"]}: '))
if boletim['média'] <= 4:
    boletim['situação']='Reprovado'
elif 5 <= boletim['média'] < 7:
    boletim['situação']='Recuperação'
else:
    boletim['situação']='Aprovado'
for k, v in boletim.items():
    print(f'{k} é {v}')
