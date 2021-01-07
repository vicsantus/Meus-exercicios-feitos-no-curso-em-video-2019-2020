n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
if n3 > n2 and n3 > n1:
    print('O número {} é o maior.'.format(n3))
elif n2 > n3 and n2 > n1:
    print('O número {} é o maior.'.format(n2))
else:
    print('O número {} é o maior.'.format(n1))
if n3 < n2 and n3 < n1:
    print('O número {} é o menor.'.format(n3))
elif n2 < n3 and n2 < n1:
    print('O número {} é o menor.'.format(n2))
else:
    print('O número {} é o menor.'.format(n1))