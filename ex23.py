cont = 0
while cont < 1:
    num = str(input('Digite um n�mero: '))
    if (float(num) < 10000) and (float(num) > 0):
        print("""Seu n�mero tem...
        {} unidade(s),
        {} dezena(s),
        {} centena(s) e
        {} unidade(s) de milhar.""".format(num[3], num[2], num[1], num[0]))
        cont += 1
    else:
        print('O n�mero deve ser maior que 0 e menor que 10000.\n')