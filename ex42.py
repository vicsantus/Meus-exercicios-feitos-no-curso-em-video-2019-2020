l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 == l3:
        print('Voc� pode formar um tri�ngulo equil�tero!')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('Voc� pode formar um tri�ngulo is�sceles!')
    else:
        print('Voc� pode formar um tri�ngulo escaleno!')
else:
    print('Voc� n�o pode formar um tri�ngulo!')