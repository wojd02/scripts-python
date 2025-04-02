n_list = []
for c in range (0,5):
    n_list.append(n = int(input('Digite um número: ')))

print(n_list)
print(f'O maior número foi {max(n_list)} que ficou no index {n_list.index(max(n_list))} e o menor valor foi {min(n_list)} que fica no index {n_list.index(min(n_list))}')
print(f'A lista em ordem númerica: {n_list.sort()}')