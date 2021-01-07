from random import randint
num = randint(1, 100)
numdesc = int(input('Tente descobrir o numero entre 1 a 100: '))
while numdesc != num:
    if numdesc < num:
        numdesc = int(input('O número é maior, tente novamente: '))
    elif numdesc > num:
        numdesc = int(input('O número é menor, tente novamente: '))
print('Você acertou, parabéns! O número era {}.'.format(num))