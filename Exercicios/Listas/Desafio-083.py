expressao = str(input('Digite uma expressão: '))
parent = []
for letter in expressao:
    if letter == '(':
        parent.append('(')
    elif letter == ')':
        if len(parent) > 0:
            parent.pop()
        else:
            parent.append(')')
            break

if len(parent) == 0:
    print('A sua expressão está correta!')
else:
    print('A sua expressão está errada!')