from time import sleep
def maior(*numeros):
    maior = cont = 0
    for numero in numeros:
        print(f'{numero}..', end=' ')
        if cont == 0:
            maior = numero
        elif maior < numero:
            maior = numero
        cont += 1
    print(f'\nForam registrados {cont} números')
    print(f'O maior valor informado foi {maior}')
maior(1, 25 ,3 ,12, 15, 0, 6)