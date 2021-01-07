val = float(input('Digite seu salário: '))
if val <= 1250:
    aum = (val * 15) / 100
    print('Com um salário de R${:.2f}, você irá ganhar um aumento de 15%. Seu novo salário'
          ' será R${:.2f}.'.format(val, val + aum))
else:
    aum = (val * 10) / 100
    print('Com um salário de R${:.2f}, você irá ganhar um aumento de 10%. Seu novo salário'
          ' será R${:.2f}.'.format(val, val + aum))