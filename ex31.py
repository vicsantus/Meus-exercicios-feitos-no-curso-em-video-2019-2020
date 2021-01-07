dis = int(input('Quantos quilometros você pretende percorrer? '))
if dis <= 200:
    pas = dis * 0.5
    print('O valor total da passagem é de \033[1;32mR${:.2f}\033[m.'.format(pas))
else:
    pas = dis * 0.45
    print('O valor total da passagem é de \033[1;34mR${:.2f}\033[m.'.format(pas))