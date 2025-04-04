dado_unit = []
pacientes = []
paciente_pesado = paciente_leve = 0
while True:
    dado_unit.append(str(input('Digite o nome do paciente: ')))
    dado_unit.append(float(input('Digite o peso do paciente: ')))
    if paciente_pesado == 0:
        paciente_pesado = dado_unit[1]
        paciente_leve = dado_unit[1]
    elif paciente_pesado < dado_unit[1]:
        paciente_pesado = dado_unit[1]
    elif paciente_leve > dado_unit[1]:
        paciente_leve = dado_unit[1]
    pacientes.append(dado_unit[:])
    dado_unit.clear()
    decisao = str(input('Deseja continuar [S/N]?: ')).upper()
    while decisao not in 'SN':
        print('Decisão inválida, tente novamente!')
        decisao = str(input('Deseja continuar [S/N]?: ')).upper()
    if decisao == 'N':
        break
print(f'\nO maior peso foi de {paciente_pesado} de', end=' ')
for c in pacientes:
    if c[1] == paciente_pesado:
        print(f'[{c[0]}]', end=' ')
print(f'\nO menor peso foi de {paciente_leve} de', end=' ')
for c in pacientes:
    if c[1] == paciente_leve:
        print(f'[{c[0]}]', end=' ')
print(f'\nO total de pessoas avaliadas foram {len(pacientes)}')