num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nova', 'dez', 'onze', 'doze',
       'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    x = int(input('Escreva um número de 0 a 20: '))
    if x < 0 or x > 20:
        print('Opção inválida!')
    else:
        break
print(f'O número {x} por extenso é {num[x]}.')