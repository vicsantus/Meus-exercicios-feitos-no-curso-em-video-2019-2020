i = int(input('Digite um número: '))
j = i
while i < (j + 10):
    print('Contagem: \033[32m{}\033[m'.format(i))
    i += 1
print('Acabou!')