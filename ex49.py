num = int(input('Digite um número: '))
for c in range(1, 11):
    mult = num * c
    print('{} x {} = {}'.format(c, num, mult), end='    ')
    adc = num + c
    print('{} + {} = {}'.format(c, num, adc))