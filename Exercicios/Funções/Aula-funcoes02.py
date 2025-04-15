def fatorial(numero=0): #igualando o parametro a 0 ele se torna opcional
    f=1 #varialve local (Não existe no código principal)
    for c in range (numero, 0, -1):
        f *= c
    return f  #meu F virou o fat5 no código principal (o return serve para transportar valores, mas as coisas ainda ocorrem normalmente dentro da função com prints)
def par(n):
    if n % 2 == 0:
        return True
    else:
        return False
fat5 = fatorial(5)
print(fat5)
#print(f) # ela não existe no escopo global
num = int(input('Digite um número: '))
if par(num):
    print(f'{num} é PAR!')
else:
    print(f'{num} é IMPAR!')