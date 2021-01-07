vel = int(input('Digite a velocidade estimada: '))
if vel <= 80:
    print('Você não foi multado')
else:
    valorm = (vel-80)*7
    print('Você passou da velocidade permitida e foi multado. Você erá pagar R${:.2f} pela sua ousadia.'.format(valorm))