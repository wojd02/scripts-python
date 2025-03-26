#Empréstimo banco (casa) - desafio 036========================================================================================
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

#Conversão decimal para binário, octal e hexadecimal - desafio 037=========================================================================
#n = int(input('Digite um número que deseja ter a conversão: '))
#conv = int(input('Você deseja converter esse número para [1] Binário, [2] octal ou [3] hexadecimal :'))

#if conv == 1:
#    binario = bin(n)[2:]
#    print('O número {} convertido em binário é {}'.format(n, binario))
#elif conv == 2:
#    octal = oct(n)[2:]
#    print('O número {} convertido em octal é {}'.format(n, octal))
#else:
#    hexadecimal = hex(n)[2:]
#    print('O número {} convertido em hexadecimal é {}'.format(n, hexadecimal))

#Comparando dois valores - desafio 038=====================================================================================================
#n1 = int(input('Digite o primeiro valor: '))
#n2 = int(input('Digite o segundo valor: '))

#if n1 > n2:
#    print('O primeiro valor é maior')
#elif n2 > n1:
#    print('O segundo valor é maior')
#else:
#    print('Os valores são iguais')

#Alistamento - Desafio 039 ====================================================================
#ano_nascimento = int(input('Em qual ano você nasceu?: '))
#idade = 2025 - ano_nascimento

#if idade < 18:
#    print('Ainda não chegou sua hora de se alistar')
#    print('Fique atento no prazo, ainda faltam {} anos'.format(18 - idade))
#elif idade == 18:
#    print('Está na hora de se alistar')
#    print('Venha á JSM mais próxima de você e tenha em mãos sua certidão de nascimento.')
#else:
#    print('Já passou do seu tempo de alistamente, se apresente a junta militar mais próxima para regularizar sua situação ')
#    print('Já passou {} ano do seu alistamento obrigatório'.format(idade - 18))

#Calculo média aluno - Desafio 040================================================================================================
#n1 = float(input('Digite a nota do primeiro semestre: '))
#n2 = float(input('Digite a nota do segundo semestre: '))
#med = (n1 + n2) / 2

#if med >= 7.0:
#    print('PARABÉNS! Você foi aprovado com uma média de {:.1f}'.format(med))
#elif med >=5.0 and med <=6.9:
#    print('CUIDADO! Você esta em recuperação, sua média foi {:.1f}'.format(med))
#else:
#    print('NÃO FOI DESSA VEZ! Você foi reprovado com uma média de {:.1f}'.format(med))

#Inscrição Natação - Desafio 041================================================================================
#ano_nascimento = int(input('Em que ano você nasceu?: '))
#idade = 2025 - ano_nascimento

#if idade <= 0 and idade <= 9:
#    print('CATEGORIA: Mirim')
#elif idade > 9 and idade <= 14:
#    print('CATEGORIA: Infantil')
#elif idade > 14 and idade <= 19:
#    print('CATEGORIA: Junior')
#elif idade >19 and idade <= 20:
#    print('CATEGORIA: Sênior')
#else:
#    print('CATEGORIA: Master')

#Desafio #35 part 2==========================================================================================
#n1 = int(input('Digite a primeira reta do triangulo: '))
#n2 = int(input('Digite o segunda reta do triangulo: '))
#n3 = int(input('Digite o terceira reta do triangulo: '))
#if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
#    print('As retas podem formar um triângulo')
#else:
#    print('As retas não podem formar um triangulo')

#if n1 == n2 and n2 == n3:
#    print('O triângulo é EQUILÁTERO!')
#elif n1 == n2 or n1 == n3 or n3 == n2 and n1 != n2 or n1 !=n3 or n3!= n2:
#    print('O triângulo é ISÓCELES')
#else:
#    print('O triângulo é ESCALENO')

#Calculadora de IMC - Desafio 043====================================================================================================
#peso = float(input('Qual o seu peso atual?: '))
#altura = float(input('Qual sua altura atual?: '))

#imc = peso / (altura * altura)

#print('Seu imc é {:.1f} e isso indica estado de'.format(imc))
#if imc < 18.5:
#    print('Abaixo do peso')
#elif imc >= 18.5 and imc < 25.0:
#    print('Peso ideal')
#elif imc >= 25.0 and imc < 30.0:
#    print('Sobrepeso')
#elif imc >= 30.0 and imc < 40.0:
#    print('Obesidade')
#else:
#    print('Obesidade mórbida')

#Calculando preços produto - Desafio 044===========================================================================================================================
#val_prod = float(input('Qual o valor do produto?: '))
#transacao = int(input('Qual o método de pagamento?:\n[1] - Á vista (Dinheiro/Cheque)\n[2] - Á vista (Cartão)\n[3] - 2x no cartão\n[4] - 3x ou mais no cartão'))

#if transacao == 1:
#    print('O valor do produto fica R${} á vista no dinheiro/cheque'.format(val_prod - (val_prod * 10) / 100))
#elif transacao == 2:
#    print('O valor do produto fica R${} á vista no cartão'.format(val_prod - (val_prod * 5) / 100))
#elif transacao == 3:
#    print('O valor do produto fica R${} em duas parcelas de R${}'.format(val_prod, val_prod/2))
#else:
#    parcelas = int(input('Quantas parcelas você quer fazer?: '))
#    novo_val_prod = val_prod + (val_prod * 20) / 100
#    print('O valor do produto fica R${} em {} parcelas de R${}'.format(novo_val_prod, parcelas, novo_val_prod / parcelas))

#PEDRA, PAPEL OU TESOURA - desafio 045 ==================================================================================================================
import random
import time
escolha_usuario = str(input('Já escolhi o meu, qual você escolhe: pedra, papel ou tesoura: '))
lista_pc = ['pedra', 'papel', 'tesoura']

escolha_pc = random.choice(lista_pc)
print('Pedra, papel ou tesoura...')
time.sleep(2)
if escolha_usuario == 'pedra':
    if escolha_pc == 'papel':
        print('Papel, EU VENCI')
    elif escolha_pc == 'tesoura':
        print('Tesoura, VOCÊ VENCEU')
    else:
        print('Pedra, EMPATAMOS')
if escolha_usuario == 'papel':
    if escolha_pc == 'tesoura':
        print('Tesoura, EU VENCI')
    elif escolha_pc == 'pedra':
        print('Pedra, VOCÊ VENCEU')
    else:
        print('Papel, EMPATAMOS')
if escolha_usuario == 'tesoura':
    if escolha_pc == 'pedra':
        print('Pedra, EU VENCI')
    elif escolha_pc == 'papel':
        print('Papel, VOCÊ VENCEU')
    else:
        print('Tesoura, EMPATAMOS')
