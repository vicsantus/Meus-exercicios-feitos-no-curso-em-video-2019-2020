dias = int(input('Quantos dias o carro ficou alugado? '))
kms = float(input('Quantos kilometros foram rodados com o carro? '))
vdias = dias * 60
vkms = kms * 0.15
total = vdias + vkms
print('O total a ser pago por {} dias de aluguel, e {} K/ms rodados será R${:.2f}'.format(dias, kms, total))