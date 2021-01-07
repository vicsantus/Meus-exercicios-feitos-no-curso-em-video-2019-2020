def leiaInt(num):
    while True:
        try:
            num = int(num)
            break
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
            num = input('Digite um número inteiro: ')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados.\033[m')
    return num


def leiaFloat(num):
    num = num.replace(',', '.')
    while True:
        try:
            num = float(num)
            break
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um número real válido.\033[m')
            num = input('Digite um número real: ')
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não informar os dados.\033[m')
    return num


n = leiaInt(input('Digite um número inteiro: '))
print(f'Você acabou de digitar o número {n}.')
n = leiaFloat(input('Digite um número real: '))
print(f'Você acabou de digitar o número {n:.1f}.')