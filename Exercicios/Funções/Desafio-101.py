def voto(ano):
    from datetime import date #Colocar biblioteca dentro da função
    idade = date.today().year - ano
    if 16 <= idade <= 18 or idade >= 70:
        return print(f'com {idade} anos o voto é FACULTATIVO')
    elif idade > 18:
        return print(f'Com {idade} anos o voto é OBRIGATÓRIO')
    elif idade < 16:
        return print(f'Com {idade} anos o voto é NEGADO')
nasc = int(input('Ano de nascimento: '))
print(voto(nasc))