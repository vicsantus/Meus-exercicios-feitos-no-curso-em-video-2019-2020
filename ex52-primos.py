num = int(input('Digite um número: '))
d = 0
for c in range(1, num+1):
    if num % num == 0 and num % 1 == 0 and num % c == 0:
        d += 1
if d == 2:
    print('O número {} é primo.'.format(num))
else:
    print('O número {} não é primo.'.format(num))