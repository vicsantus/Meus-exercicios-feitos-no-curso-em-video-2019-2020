val = float(input('Qual o valor da resid�ncia?: '))
sal = float(input('Qual o valor do seu sal�rio l�quido mensal?: '))
tempo = int(input('Em quantos anos voc� pretende pagar?: '))
prestmes = val / (tempo * 12)
if prestmes > ((sal * 30)/100):
    print('\033[1;4;31mEmpr�stimo negado.\033[m Voc� n�o pode comprar essa resid�ncia!')
else:
    print('Voc� ir� pagar o valor de \033[1;32mR${:.2f}\033[m por m�s, para comprar essa resid�ncia.'.format(prestmes))