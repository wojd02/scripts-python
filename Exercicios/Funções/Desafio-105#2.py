def notas(*nota, sit = False):
    """
    >>Função NOTAS serve para avaliar diversas notas e entregar a situação da turma<<
    :param n: nota/notas dos alunos(aceita várias)
    :param sit: valor opcional, indica se deve ou não adicionar a situação da média da turma
    :return: um dicionário contendo diversas informações da turma gerada com o processamento das notas.
    """
    r = dict()
    r['quantidade'] = len(nota)
    r['maxima'] = max(nota)
    r['menor'] = min(nota)
    r['media'] = sum(nota) / len(nota)
    if sit == True:
        if r['media'] <= 5:
            r['situação'] = 'RUIM'
        elif 5 < r['media'] < 7:
            r['situação'] = 'OK'
        else:
            r['situação'] = 'ÓTIMO'
    if sit == False:
        sit = ''
    return r
resp = notas(5.5, 6.0, 10, 3.5, 5)
print(resp)
help(notas)


