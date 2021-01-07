from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Você pertence a categoria MIRIM.')
elif 9 < idade <= 14:
    print('Você pertence a categoria INFANTIL.')
elif 14 < idade <= 19:
    print('Você pertence a categoria JUNIOR.')
elif 19 < idade <= 25:
    print('Você pertence a categoria SÊNIOR.')
else:
    print('Você pertence a categoria MASTER.')