vel = int(input('Digite a velocidade estimada: '))
if vel <= 80:
    print('Voc� n�o foi multado')
else:
    valorm = (vel-80)*7
    print('Voc� passou da velocidade permitida e foi multado. Voc� er� pagar R${:.2f} pela sua ousadia.'.format(valorm))