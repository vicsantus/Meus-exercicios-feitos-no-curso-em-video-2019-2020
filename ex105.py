def notas(*args, sit=False):
    """
    -> Fun��o para analisar notas e situa��es de v�rios alunos.
    :param args: O argumento pode ser 1 s�, ou varios. args s�o os valores para o calculo.
    :param sit: Situa��o mostra se est� boa, ruim ou razo�vel a situa��o do aluno. Passivel de passar ou n�o.
    :return: Todas as informa��es s�o colocadas em um dicion�rio e o dicion�rio � retornado.
    """
    dici = {'total': len(args), 'maior': max(args), 'menor': min(args), 'm�dia': f'{(sum(args) / len(args)):.2f}'}
    if sit:
        media = sum(args) / len(args)
        if media < 5:
            dici['situa��o'] = 'RUIM'
        elif 5 <= media < 7:
            dici['situa��o'] = 'RAZO�VEL'
        else:
            dici['situa��o'] = 'BOA'
    return dici


resp = notas(5.5, 2.5, 9.8, 10, sit=True)
print(resp)