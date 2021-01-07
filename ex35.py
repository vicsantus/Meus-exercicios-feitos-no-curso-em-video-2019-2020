l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    print('Os segmentos podem formar um triângulo!')
else:
    print('Os segmentos não podem formar um triângulo!')