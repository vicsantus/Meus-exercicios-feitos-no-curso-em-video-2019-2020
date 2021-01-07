val = float(input('Qual o valor da residência?: '))
sal = float(input('Qual o valor do seu salário líquido mensal?: '))
tempo = int(input('Em quantos anos você pretende pagar?: '))
prestmes = val / (tempo * 12)
if prestmes > ((sal * 30)/100):
    print('\033[1;4;31mEmpréstimo negado.\033[m Você não pode comprar essa residência!')
else:
    print('Você irá pagar o valor de \033[1;32mR${:.2f}\033[m por mês, para comprar essa residência.'.format(prestmes))