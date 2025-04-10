from datetime import datetime
ficha = dict()
ficha['nome'] = str(input('Nome: '))
ficha['ano'] = int(input('Ano de nascimento: '))
ficha['cdt'] = int(input('Carteira de trabalho (0 não tem): '))
ficha['idade'] = datetime.now().year - ficha['ano']
if ficha['cdt'] != 0:
    ficha['contrato'] = int(input('Ano de contratação: '))
    ficha['salario'] = float(input('Salário: '))
    ficha['aposentadoria'] = ((ficha['contrato'] + 35) - datetime.now().year)
print('-=' * 40)
print(ficha)
for v in ficha:
    print(f'{v} tem o valor {ficha[v]}')

#Outra forma de fazer o esquema de repetição
#for v, k in ficha.items():
#    print(f' - {v} tem o valor {k}')
