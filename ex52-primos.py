num = int(input('Digite um n�mero: '))
d = 0
for c in range(1, num+1):
    if num % num == 0 and num % 1 == 0 and num % c == 0:
        d += 1
if d == 2:
    print('O n�mero {} � primo.'.format(num))
else:
    print('O n�mero {} n�o � primo.'.format(num))