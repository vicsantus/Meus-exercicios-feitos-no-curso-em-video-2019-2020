preco = float(input('Qual o pre�o dessa pora? R$'))
desc = float(input('Qual o valor do desconto? '))
val = (preco * desc) / 100
print('O valor que antes era de R${:.2f}, com um desconto de {:.0f}%, voc� ira '
      'pagar o valor de R${:.2f}.'.format(preco, desc, preco-val))