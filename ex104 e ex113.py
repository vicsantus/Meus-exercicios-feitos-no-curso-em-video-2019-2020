def leiaInt(num):
    while True:
        try:
            num = int(num)
            break
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Digite um n�mero inteiro v�lido.\033[m')
            num = input('Digite um n�mero inteiro: ')
        except KeyboardInterrupt:
            print('\033[31mO usu�rio preferiu n�o informar os dados.\033[m')
    return num


def leiaFloat(num):
    num = num.replace(',', '.')
    while True:
        try:
            num = float(num)
            break
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um n�mero real v�lido.\033[m')
            num = input('Digite um n�mero real: ')
        except KeyboardInterrupt:
            print('\033[31mO usu�rio preferiu n�o informar os dados.\033[m')
    return num


n = leiaInt(input('Digite um n�mero inteiro: '))
print(f'Voc� acabou de digitar o n�mero {n}.')
n = leiaFloat(input('Digite um n�mero real: '))
print(f'Voc� acabou de digitar o n�mero {n:.1f}.')