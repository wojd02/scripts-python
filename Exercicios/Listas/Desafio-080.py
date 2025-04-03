valores = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
        print('Adicionando o número ao final da lista...')
    else:
        cont = 0
        while cont < len(valores):
            if n <= valores[cont]:
                valores.insert(cont, n)
                print(f'Adicionando o número na casa {cont}...')
                break
            cont += 1
print(valores)