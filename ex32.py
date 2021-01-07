ano = int(input('Digite um ano: '))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 4 != 0 and ano % 400 == 0):
    print('\033[4;33mO ano de {} é bissexto.'.format(ano))
else:
    print('\033[4;31mO ano de {} não é bissexto.'.format(ano))