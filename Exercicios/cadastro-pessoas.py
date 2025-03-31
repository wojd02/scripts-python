from time import sleep
cont_mais_18 = cont_homem = cont_mulher = 0
decisao = 'S'

while True:
    print('-' * 30)
    print('Cadastre uma pessoa:')
    print('-' * 30)
    if decisao == 'S':
        sexo = str(input('Qual o sexo da pessoa? [F/M]: ')).upper().strip()[0]
        while sexo not in 'FM':
            print('Decisão inválida, tente novamente!')
            sexo = str(input('Qual o sexo da pessoa? [F/M]: ')).upper()
        idade = int(input('Qual a idade da pessoa?: '))
        decisao = str(input('Gostaria de continuar? [S/N]')).upper()
        while decisao not in 'SN':
            print('Decisão inválida, tente novamente!')
            decisao = str(input('Gostaria de continuar? [S/N]')).upper()
        if idade >= 18:
            cont_mais_18 += 1
        if sexo == 'M':
            cont_homem += 1
        if sexo == 'F' and idade <= 20:
            cont_mulher += 1
    else:
        print('ENCERRANDO O PROGRAMA...')
        sleep(1)
        break
print(f'Tiveram {cont_mais_18} pessoas com mais de 18 anos')
print(f'Tiveram {cont_homem} homens cadastrados')
print(f'Foram cadastradas {cont_mulher} mulheres com menos de 20 anos')
