mortuario = list()
def mortuario_sistema(nome, idade, hora, r_autopsia):
    sistema = dict()
    from datetime import date
    sistema['nome'] = nome
    sistema['idade'] = idade
    sistema['hora'] = hora
    sistema['data nascimento'] = date.today().year - sistema['idade']
    sistema['data morte'] = (f'{date.today().day}/{date.today().month}/{date.today().year}')
    sistema['Causa da morte'] = r_autopsia
    mortuario.append(sistema)
    return sistema
def procura(nome):
    for c in mortuario:
        if nome == c['nome']:
            print(c)

#Sistema de entrada
mortuario_sistema('Andre Souza', 38, '15:30pm', 'ataque cardiaco')
mortuario_sistema('Maria Luz Soares', 24, '19:00pm', 'homicidio')
print(mortuario)
print('-' * 100)

procura('Maria Luz Soares')
print('-' * 100)

mortuario_sistema('Carla Andrade', 69, '12:30am', 'Causas Naturais')
print(mortuario)
print('-' * 100)

procura('Andre Souza')


