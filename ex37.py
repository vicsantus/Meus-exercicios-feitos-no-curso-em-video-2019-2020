from time import sleep
num = int(input('Digite um numero: '))
num1 = num
rep = 0
while rep < 1:
    conv = int(input("""Escolha uma base para convers�o:
\033[31mBin�rio digite 1\033[m, 
\033[32mOctal digite 2\033[m, 
\033[33mHexadecimal digite 3:\033[m
Sua op��o: """))
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
        print('Voc� n�o digitou uma op��o v�lida.')
print('Seu n�mero {} convertido, � igual � {}.'.format(num1, num[2:]))
sleep(3)