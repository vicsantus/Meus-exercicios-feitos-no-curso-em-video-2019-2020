preco = float(input('Qual o pre�o do produto?: '))
print('''Qual a forma de pagamento?
[0] A vista/dinheiro
[1] D�bito
[2] Cr�dito''')
rep = 0
while rep < 1:
    cond = int(input('Escolha uma op��o: '))
    if cond == 0:
        desc = (preco * 10) / 100
        total = preco - desc
        rep += 1
    elif cond == 1:
        desc = (preco * 5) / 100
        total = preco - desc
        rep += 1
    elif cond == 2:
        parc = int(input('Em quantas vezes voc� quer parcelar?: '))
        if parc >= 3:
            jus = (preco * 20) / 100
            total = preco + jus
            rep += 1
        else:
            total = preco
            rep += 1
    else:
        print('Op��o inv�lida!')
print('Voc� ir� pagar o valor total de \033[1;4;31mR${:.2f}\033[m.'.format(total))