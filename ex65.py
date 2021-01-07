cont = 0
num = maior = media = soma = ant = 0
menor = 1000 * 1000 * 1000 * 1000
sair = 'S'
while sair == 'S':
    cont += 1
    print(cont)
    ant = num
    print(ant)
    num = int(input('Digite um valor: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    soma += num
    media = soma / cont
    val = 0
    while val == 0:
        sair = str(input('Deseja continuar?[S/N]: ')).upper()
        if sair != 'S' and sair != 'N':
            print('Opção inválida!')
            print('Digite apenas "S" para sim, e "N" para não.')
        else:
            val += 1
print('Foram digitados {} numeros.'.format(cont))
print('A soma deles é igual á {}.'.format(soma))
print('A média entre eles é igual á {:.2f}.'.format(media))
print('O maior número é igual á {}.'.format(maior))
print('O menor número é igual á {}'.format(menor))