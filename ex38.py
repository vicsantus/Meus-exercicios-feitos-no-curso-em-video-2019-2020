n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O número {} é o maior.'.format(n1))
elif n2 > n1:
    print('O número {} é o maior.'.format(n2))
else:
    print('Os dois número possuem o mesmo tamanho.')