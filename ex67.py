def msg():
    print('\033[33mDigite qualquer valor negativo para sair.\033[m')


print('Para aparecer a mensagem abaixo, a qualquer momento, digite "0".')
msg()
while True:
    num = int(input('\nDigite um número para descobrir sua tabuada: '))
    if num == 0:
        msg()
    elif num < 0:
        break
    elif num > 0:
        for c in range(1, 11):
            print(f'{c} x {num} = {c * num}')
print('\033[31;1mFIM!!!\033[m')