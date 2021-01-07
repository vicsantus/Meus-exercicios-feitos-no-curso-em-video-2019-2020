from random import shuffle

n1 = str(input('Digite o nome do primeiro trouxa: '))
n2 = str(input('Digite o nome do segundo trouxa: '))
n3 = str(input('Digite o nome do terceiro trouxa: '))
n4 = str(input('Digite o nome do quarto trouxa: '))
nomes = [n1, n2, n3, n4]
shuffle(nomes)
print('A ordem de apresentação será {}.'.format(nomes))