f= c = cont = cont_par = cont_3 = 0
valores = tuple(int(input('Digite um número: ')) for c in range (0,4))
print(valores)

for c in range (0, len(valores)):
    if valores[c] == 9:
        cont += 1
    if valores[c] % 2 == 0:
        cont_par += 1
    if valores[c] == 3:
        cont_3 = c
print(f'Tiveram {cont} números 9 na tupla')
print(f'O número 3 apareceu na {cont_3} casa')
print(f'Tiveram {cont_par} números pares')