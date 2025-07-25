import pandas as pd
from IPython.display import display

#Fazendo um dataframe com dicionario
df1 = pd.DataFrame({
    'Product ID': [1, 2, 3, 4],
    'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
    'Color': ['blue', 'green', 'red', 'black']
})

print(df1)
print()

#Fazendo um dataframe com lista
print()
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]],
  columns=['Store ID', 'Location', 'Number of Employees'])

print(df2)
print()

cursos_tabela = pd.read_excel("C:/Users/Windows 11/Desktop/cursos_teste.xlsx")
display(cursos_tabela)
print()
display(cursos_tabela.head()) #O .head(n de linhas) mostra as 5 primeiras(se n tiver outro numero no parenteses) linhas da tabela 
print(cursos_tabela.shape) #mostra o numero de linhas e colunas
print(cursos_tabela.describe()) #mostra dados da tabela
tipos_curso = cursos_tabela[['Curso', 'Nomes']] #selecionando colunas para aparecer
print(tipos_curso)
print()
print(cursos_tabela.loc[cursos_tabela['Curso'] == 'Artes visuais']) #selecionando elementos na tabela
#cursos_tabela.loc[linhas, colunas] estrutura do LOC
print()
print(cursos_tabela.loc[cursos_tabela['Curso'] == 'Filosofia', ['Nomes', 'email', 'status aula']])
cursos_tabela['Mês entrada'] = 0
print(cursos_tabela)
cursos_tabela.loc[[1,7,5,9], ['Mês entrada']] = 'fev'
cursos_tabela.loc[[0,8,6,3], ['Mês entrada']] = 'dez'
print(cursos_tabela)
cursos_tabela = cursos_tabela.drop('Mês entrada', axis=1) #axis=0 (linha) / axis=1 (coluna)
print(cursos_tabela)

