from math import hypot

cop = float(input('Digite o cateto oposto: '))
cad = float(input('Digite o cateto adjacente: '))
hipo = hypot(cop, cad)
print('A hipotenusa é igual a {:.2f}.'.format(hipo))