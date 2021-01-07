num = []
while True:
    num2 = (int(input('Digite um número: ')))
    if num.count(num2):
        print(f'Número {num2} já foi adicionado!')
    else:
        num.append(num2)
    while True:
        cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()
        if cont in 'NS':
            break
        else:
            print('Opção inválida!')
    if cont == 'N':
        break
num.sort()
print(f'Você digitou os valores {num}.')