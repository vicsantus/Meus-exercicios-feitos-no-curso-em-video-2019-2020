m = int(input('Qual o tamanho do seu chifre em metros: '))
print('Seu corno é de \033[1;32m{}m\033[m, \033[1;33m{}cm\033[m e \033[1;31m{}mm\033[m.'.format(m, m * 100, m * 1000))