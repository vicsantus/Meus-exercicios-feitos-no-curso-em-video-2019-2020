from datetime import date
ano = int(input('Digite o ano do seu nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Voc� pertence a categoria MIRIM.')
elif 9 < idade <= 14:
    print('Voc� pertence a categoria INFANTIL.')
elif 14 < idade <= 19:
    print('Voc� pertence a categoria JUNIOR.')
elif 19 < idade <= 25:
    print('Voc� pertence a categoria S�NIOR.')
else:
    print('Voc� pertence a categoria MASTER.')