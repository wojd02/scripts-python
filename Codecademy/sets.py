genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 'pop', 'rap', 'latin']

#Tornando a lista genre_results em um set
genre_survey = set(genre_results)
print(genre_survey)

#formatando o set (Para aparecer apenas as 3 primeiras letras do elemento)
form_survey = {genre[0:3] for genre in genre_survey}
print(form_survey)

#Criando um Frozenset (não pode ser modificado)
lista = ['Junior', 'Andre', 'Carlos', 'Ana', 'Maria', 'Kara', 'Anthonny']
set_2 = frozenset(lista)
print(set_2)

#Atualizando um SET
names = {'Users_names':['Junior', 'Andre', 'Carlos', 'Ana', 'Maria', 'Kara', 'Anthonny']}

att_1 = 'Eduardo'
att_2 = 'Helena'
att_3 = 'Karen'
att_4 = 'Eduardo'
print(names)
list_att = [att_1, att_2, att_3, att_4]
names_set = set(names['Users_names']) #Precisa converter ele para um set para usar o update, pois no NAMES ele funciona como dicionario
names_set.update(list_att)
names['Users_names'] = names_set
print(names)
