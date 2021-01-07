nome = str(input('Digite um nome completo: '))
n = nome
n = n.lower()
if 'silva' in n:
    print('Existe "Silva" no nome {}.'.format(nome.title()))
else:
    print('Não existe "Silva" no nome {}.'.format(nome.title()))