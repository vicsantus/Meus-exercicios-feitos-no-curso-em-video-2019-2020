num = []
while True:
    num2 = (int(input('Digite um n�mero: ')))
    if num.count(num2):
        print(f'N�mero {num2} j� foi adicionado!')
    else:
        num.append(num2)
    while True:
        cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()
        if cont in 'NS':
            break
        else:
            print('Op��o inv�lida!')
    if cont == 'N':
        break
num.sort()
print(f'Voc� digitou os valores {num}.')