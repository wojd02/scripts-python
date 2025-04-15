def leiaINT(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric() == True:
            valor = int(n)
            ok = True
        else:
            print('Mensagem inválida, digite um número por gentileza!')
        if ok:
            break
    return valor
n = leiaINT('Digite um número: ')
print(n)

