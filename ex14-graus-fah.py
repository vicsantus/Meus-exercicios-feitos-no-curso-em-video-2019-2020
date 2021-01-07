r = 0
while r < 1:
    qual = input('Você quer converter graus, ou fahrenheit (G/F)? ')
    if qual == 'G' or qual == 'g':
        conv = float(input('Qual o valor em graus? '))
        fah = ((conv * 9) / 5) + 32
        print('O valor de {}° Graus é igual a {:.1f}° Fahrenheit!'.format(conv, fah))
        r += 1
    elif qual == 'F' or qual == 'f':
        conv = float(input('Qual o valor em fahrenheit? '))
        graus = ((conv - 32) * 5) / 9
        print('O valor de {}° Fahrenheit é igual a {:.1f}° Graus!'.format(conv, graus))
        r += 1
    else:
        print('\nDigite "G" para graus, ou "F" para fahrenheit.\n')