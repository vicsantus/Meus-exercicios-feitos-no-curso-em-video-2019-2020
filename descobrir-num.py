from random import randint
num = randint(1, 100)
numdesc = int(input('Tente descobrir o numero entre 1 a 100: '))
while numdesc != num:
    if numdesc < num:
        numdesc = int(input('O n�mero � maior, tente novamente: '))
    elif numdesc > num:
        numdesc = int(input('O n�mero � menor, tente novamente: '))
print('Voc� acertou, parab�ns! O n�mero era {}.'.format(num))