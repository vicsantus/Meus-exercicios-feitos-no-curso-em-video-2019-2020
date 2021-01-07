nome = str(input('Digite seu nome completo: '))
nome = nome.title()
nome = nome.split()
pnome = nome[0]
nome.reverse()
uno = nome[0]
print('Bem-vindo(a) {} {}!'.format(pnome, uno))