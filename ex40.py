n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
if med < 5:
    print('Sua m�dia � de \033[31m{}\033[m. Voc� foi \033[1;4;31mREPROVADO\033[m!'.format(med))
elif 5 <= med < 7:
    print('Sua m�dia � de \033[33m{}\033[m. Voc� est� em \033[1;4;33mRECUPERA��O\033[m!'.format(med))
else:
    print('Sua m�dia � de \033[36m{}\033[m. Parab�ns! Voc� foi \033[1;4;36mAPROVADO\033[m!'.format(med))