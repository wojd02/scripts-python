def ExistArq(nome):
    try:
        test = open(nome, 'rt')
        test.close()    
    except (FileNotFoundError):
        return False
    else:
        return True


def CriarArq(nome):
    try:
        test = open(nome, 'wt+')
        test.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def LerArq(nome):
    try:
        test = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        print('-' * 45)
        print(f'{'PESSOAS CADASTRADAS':^45}')
        print('-' * 45)
        for linha in test:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<36}{dado[1]:>3} anos')
    finally:
        test.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        test = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            test.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na integração de dados')
        else:
            print(f'Novo registro integrado!')
            test.close()