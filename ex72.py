num = ('zero', 'um', 'dois', 'tr�s', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nova', 'dez', 'onze', 'doze',
       'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    x = int(input('Escreva um n�mero de 0 a 20: '))
    if x < 0 or x > 20:
        print('Op��o inv�lida!')
    else:
        break
print(f'O n�mero {x} por extenso � {num[x]}.')