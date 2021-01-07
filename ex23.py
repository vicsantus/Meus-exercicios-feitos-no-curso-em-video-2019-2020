cont = 0
while cont < 1:
    num = str(input('Digite um número: '))
    if (float(num) < 10000) and (float(num) > 0):
        print("""Seu número tem...
        {} unidade(s),
        {} dezena(s),
        {} centena(s) e
        {} unidade(s) de milhar.""".format(num[3], num[2], num[1], num[0]))
        cont += 1
    else:
        print('O número deve ser maior que 0 e menor que 10000.\n')