val = float(input('Digite seu sal�rio: '))
if val <= 1250:
    aum = (val * 15) / 100
    print('Com um sal�rio de R${:.2f}, voc� ir� ganhar um aumento de 15%. Seu novo sal�rio'
          ' ser� R${:.2f}.'.format(val, val + aum))
else:
    aum = (val * 10) / 100
    print('Com um sal�rio de R${:.2f}, voc� ir� ganhar um aumento de 10%. Seu novo sal�rio'
          ' ser� R${:.2f}.'.format(val, val + aum))