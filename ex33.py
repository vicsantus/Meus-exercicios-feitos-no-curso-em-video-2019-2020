n1 = int(input('Digite o primeiro n�mero: '))
n2 = int(input('Digite o segundo n�mero: '))
n3 = int(input('Digite o terceiro n�mero: '))
if n3 > n2 and n3 > n1:
    print('O n�mero {} � o maior.'.format(n3))
elif n2 > n3 and n2 > n1:
    print('O n�mero {} � o maior.'.format(n2))
else:
    print('O n�mero {} � o maior.'.format(n1))
if n3 < n2 and n3 < n1:
    print('O n�mero {} � o menor.'.format(n3))
elif n2 < n3 and n2 < n1:
    print('O n�mero {} � o menor.'.format(n2))
else:
    print('O n�mero {} � o menor.'.format(n1))