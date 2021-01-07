n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
if med < 5:
    print('Sua média é de \033[31m{}\033[m. Você foi \033[1;4;31mREPROVADO\033[m!'.format(med))
elif 5 <= med < 7:
    print('Sua média é de \033[33m{}\033[m. Você está em \033[1;4;33mRECUPERAÇÃO\033[m!'.format(med))
else:
    print('Sua média é de \033[36m{}\033[m. Parabéns! Você foi \033[1;4;36mAPROVADO\033[m!'.format(med))