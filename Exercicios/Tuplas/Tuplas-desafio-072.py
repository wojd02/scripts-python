#lanche = 'pizza', 'hambúrguer', 'suco', 'pudim'
#for pos, comida in enumerate(lanche):
#    print(f'Vou comer {comida} na posição {pos}')

#for comida in range (0, len(lanche)):
#    print(f'Vou comer {lanche[comida]} na posição {comida}')

#Desafio 72 - Passando número para extenso

contagem = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete','oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

escolha = int(input('Escolha um número entre 0 a 20: '))
while True:
    if escolha not in range (0,20):
        print('Escolha inválida, tenta novamente!')
        escolha = int(input('Escolha um número entre 0 a 20: '))
    elif escolha in range (0,20):
        break
print(contagem[escolha])


