from time import sleep
def contador(inicio, fim, passo):
    if inicio < fim:
        if passo > 0:
            for c in range(inicio, fim + 1, passo):
                print(f'{c}..', end=' ')
                sleep(0.5)
        elif passo < 0:
            for c in range(inicio, fim + 1, passo * -1):
                print(f'{c}..', end=' ')
                sleep(0.5)
    elif inicio > fim:
        if passo < 0:
            for c in range(inicio, fim - 1, passo):
                print(f'{c}..', end=' ')
                sleep(0.5)
        elif passo > 0:
            for c in range(inicio, fim - 1, passo * -1):
                print(f'{c}..', end=' ')
                sleep(0.5)
    print()
contador(1, 10, 1)
contador(10, 0, -2)
a = int(input('Primeiro valor: '))
b = int(input('último número: '))
c = int(input('passo: '))
contador(a, b, c)