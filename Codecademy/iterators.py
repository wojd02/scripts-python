import itertools
num = int(input('Digite um número: '))
for c in itertools.count(0,2):
    print(c)
    if c >= num:
        break