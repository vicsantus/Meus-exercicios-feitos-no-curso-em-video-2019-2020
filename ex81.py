lista = list()
while True:
    lista.append(int(input('Digite um n�mero: ')))
    while True:
        conti = str(input('Deseja continuar [S/N]: ')).upper().strip()
        if conti in 'SN':
            break
        else:
            print('Op��o inv�lida!\n')
    if conti == 'N':
        break
print(f'Foram digitados {len(lista)} valores.')
lista.sort(reverse=True)
print(f'Os valores s�o {lista}.')
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 n�o faz parte a lista.')