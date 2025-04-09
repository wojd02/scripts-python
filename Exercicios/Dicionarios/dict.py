pessoas = {'nome': 'Jonatan', 'Idade': 23, 'Idioma': 'PT-BR'}
print(pessoas['nome'])
print(pessoas['Idade'])
print(pessoas.values()) #Conteúdo do tópico
print(pessoas.keys()) #Seriam tipo os tópicos do dicionario
print(pessoas.items()) #Funciona como se fosse uma tupla dentro de uma lista(junção value + key)
pessoas['Localização']= 'Lajeado'
print(pessoas.keys())
