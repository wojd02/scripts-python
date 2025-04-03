expressao = str(input('Digite uma expressão: '))
pilha = []
for parent in expressao:
    if parent == '(':
        pilha.append('(')
    elif parent == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('A sua expressão está correta!')
else:
    print('A sua expressão está errada!')