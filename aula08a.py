import math
num = float(input('Digite um numero: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} � igual a \033[31m{}\033[m.'.format(num, math.trunc(raiz)))