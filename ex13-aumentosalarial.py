preco = float(input('Quanto é o seu salário?: R$'))
desc = float(input('Qual a porcentagem do aumento?: '))
val = (preco * desc) / 100
print('O valor que antes era de R${:.2f}, com uma porcentagem de aumento de {:.0f}%, você ira '
      'ganhar o valor de R${:.2f}.'.format(preco, desc, preco+val))