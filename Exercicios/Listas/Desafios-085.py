number_list = [[], []]
for c in range (0,7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        number_list[0].append(n)
    else:
        number_list[1].append(n)
number_list[0].sort()
number_list[1].sort()
print(f'Os números pares são {number_list[0]}')
print(f'Os números ímpares são {number_list[1]}')
