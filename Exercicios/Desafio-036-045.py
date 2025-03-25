#Empréstimo banco (casa) - desafio 036
                   #descrição
#pergunte valor casa, sálario e quantos anos vai pagar
#calcular valor prestação mensal (n pode exceder 30% do sálario)

#val_casa = float(input('Qual o valor total da casa?: '))
#sal = float(input('Qual o seu sálario atual?: '))
#tempo = float(input('Em quantos anos planeja pagar a divida?: '))

#prestacao_mensal = val_casa / (tempo * 12)
#percentual_sal = (sal * 30) / 100

#if prestacao_mensal <= percentual_sal:
    #print('Parabéns, o empréstimo foi aprovado.')
    #print('O percentual do sálario ficou dentro dos 30% R${:.3f}'.format(percentual_sal))
    #print('Ficaram {} parcelas no valor de R${:.3f}'.format(tempo*12, prestacao_mensal))
#else:
    #print('Desculpe, infelizmente o empréstimo foi negado')
    #print('O valor da prestação ficou acima da margem de 30% do seu sálario')
    #print('Seu sálario é de {:.3f} e a prestação ficou {:.3f}'.format(sal, prestacao_mensal))

n = int(input('Digite um número que deseja ter a conversão: '))

binario = bin(n)
print(f'{binario:b}'.format(binario)) 