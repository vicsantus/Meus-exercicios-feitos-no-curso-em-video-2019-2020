exp = str(input('Digite uma express�o: '))
'''aberto = exp.count('(')
fechado = exp.count(')')
exp1 = list()
exp1.append(exp)
cont = 0
while True:
    cont += 1
    if exp.rindex('(') < exp.index(')'):
        del exp1[-1::-1]'('
    if cont == aberto:
        break
    else:
        print('Essa express�o est� errada.')'''
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Essa express�o est� correta.')
else:
    print('Essa express�o est� errada.')