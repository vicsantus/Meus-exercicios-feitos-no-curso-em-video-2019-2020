n1 = int(input('Digite o primeiro n�mero: '))
n2 = int(input('Digite o segundo n�mero: '))
if n1 > n2:
    print('O n�mero {} � o maior.'.format(n1))
elif n2 > n1:
    print('O n�mero {} � o maior.'.format(n2))
else:
    print('Os dois n�mero possuem o mesmo tamanho.')