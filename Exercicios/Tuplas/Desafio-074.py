from random import randint
maior = menor = 0
pc = randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100)

print(pc[0:5])
for c in range(0, len(pc)):
    if c == 0:
        maior = pc[c]
        menor = pc[c]
    elif maior < pc[c]:
        maior = pc[c]
    elif menor > pc[c]:
        menor = pc[c]
print(f'O maior número sorteado foi {maior} e o menor foi {menor}')