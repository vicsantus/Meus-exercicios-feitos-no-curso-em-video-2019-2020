from time import sleep
num = int(input('Digite um numero: '))
num1 = num
rep = 0
while rep < 1:
    conv = int(input("""Escolha uma base para conversão:
\033[31mBinário digite 1\033[m, 
\033[32mOctal digite 2\033[m, 
\033[33mHexadecimal digite 3:\033[m
Sua opção: """))
    if conv == 1:
        num = bin(num)
        rep += 1
    elif conv == 2:
        num = oct(num)
        rep += 1
    elif conv == 3:
        num = hex(num)
        rep += 1
    else:
        print('Você não digitou uma opção válida.')
print('Seu número {} convertido, é igual á {}.'.format(num1, num[2:]))
sleep(3)