n = soma = cont_num = 0
while n != 999:
    n = int(input('Digite um valor: '))
    if n != 999:
        soma += n
        cont_num += 1
print('FIM DO PROGRAMA')
print('A soma dos números digitados foi de {}'.format(soma))
print('Foram digitados {} valores'.format(cont_num))