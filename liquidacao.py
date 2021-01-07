preco = float(input('Qual o preço dessa pora? R$'))
desc = float(input('Qual o valor do desconto? '))
val = (preco * desc) / 100
print('O valor que antes era de R${:.2f}, com um desconto de {:.0f}%, você ira '
      'pagar o valor de R${:.2f}.'.format(preco, desc, preco-val))