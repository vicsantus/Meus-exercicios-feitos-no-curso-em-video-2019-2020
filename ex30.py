num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número é \033[1;31mpar\033[m.')
else:
    print('O número é \033[1;35mímpar\033[m.')