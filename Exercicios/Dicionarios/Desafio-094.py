dados = dict()
conjunto_dados = list()
idades = list()
j_mulheres = list()
acima_idade = list()
while True:
    dados['nome'] = str(input('Nome:'))
    dados['sexo'] = str(input('Sexo [M/F]: ')).upper()
    while dados['sexo'] not in 'MF':
        print('Resposta inválida, tente novamente!')
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()
    dados['idade'] = int(input('Idade: '))
    conjunto_dados.append(dados.copy())
    dados.clear()
    decisao = str(input('Deseja continuar [S/N]: ')).upper()
    while decisao not in 'SN':
        print('Decisão inválida, tente novamente!')
        decisao = str(input('Deseja continuar [S/N]: ')).upper()
    if decisao == 'N':
        print('FINALIZANDO SISTEMA...')
        break
for c in conjunto_dados:
   idades.append(c["idade"])
for c in conjunto_dados:
    if c['sexo'] == 'F':
        j_mulheres.append(c)
media = (sum(idades)) / len(conjunto_dados)
for c in conjunto_dados:
    if c['idade'] >= media:
        acima_idade.append(c)
print(f'[A] - Foram cadastradas um total de {len(conjunto_dados)} pessoas')
print(f'[B] - A média das idades foi de {media:.1f}')
print(f'[C] - As mulheres cadastradas foram:', end=' ')
for c in j_mulheres:
    print(f'[{c["nome"]}]', end=' ')
print(f'\n[D] - Pessoas acima da média de idade:')
for c in acima_idade:
    print(f'Nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]}')