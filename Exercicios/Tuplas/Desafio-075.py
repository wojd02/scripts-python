f= c = cont = cont_par = cont_3 = 0
valores = tuple(int(input('Digite um número: ')) for c in range (0,4))
print(valores)

for c in valores:
    if c % 2 == 0:
        cont_par += 1
print(f'Tiveram {valores.count(9)} números 9 na tupla')
if 3 in valores:
    print(f'O número 3 apareceu na {valores.index(3)} casa')
else:
    print('Não foram digitados números 3 na tupla')
print(f'Tiveram {cont_par} números pares')