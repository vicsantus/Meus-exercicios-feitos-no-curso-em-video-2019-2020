def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: Número a ser calculado no fatorial.
    :param show: Permite ou nega a exposição do calculo do fatorial.
    :return: Retorna o valor final do fatorial.
    """
    f = 1
    print('--'*40)
    for c in range(num, 0, -1):
        f *= c
    if show:
        for c in range(num, 0, -1):
            if c - 1 != 0:
                print(c, end=' x ')
            else:
                print(c, end=' = ')
    return f


print(fatorial(5, True))