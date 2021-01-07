def notas(*args, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param args: O argumento pode ser 1 só, ou varios. args são os valores para o calculo.
    :param sit: Situação mostra se está boa, ruim ou razoável a situação do aluno. Passivel de passar ou não.
    :return: Todas as informações são colocadas em um dicionário e o dicionário é retornado.
    """
    dici = {'total': len(args), 'maior': max(args), 'menor': min(args), 'média': f'{(sum(args) / len(args)):.2f}'}
    if sit:
        media = sum(args) / len(args)
        if media < 5:
            dici['situação'] = 'RUIM'
        elif 5 <= media < 7:
            dici['situação'] = 'RAZOÁVEL'
        else:
            dici['situação'] = 'BOA'
    return dici


resp = notas(5.5, 2.5, 9.8, 10, sit=True)
print(resp)