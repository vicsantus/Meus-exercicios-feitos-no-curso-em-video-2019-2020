print('\033[32m=x=\033[m'*10)
print('  PROGRAMA DE CALCULO DO IMC')
print('\033[32m=x=\033[m'*10)
alt = float(input('\nDigite sua altura: '))
pes = float(input('Digite seu peso: '))
imc = pes / (alt * alt)
if imc < 18.5:
    print('Seu IMC é de {:.1f}. Você está abaixo do seu peso ideal.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.1f}. Você está no seu peso ideal.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.1f}. Você está com sobrepeso.'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.1f}. Você está com obesidade de grau 1 ou grau 2.'.format(imc))
else:
    print('Seu IMC é de {:.1f}. Você está com obesidade de grau 3. Procure emagrecer imediatamente.'.format(imc))