from datetime import date
foi = 0
nfoi = 0
print('Voc� vai escrever o ano de nascimento de 7 pessoas!!')
print('O programa vai calcular quantas atingiram a maior idade, e quantas n�o atingiram.')
for c in range(0, 7):
    ano = int(input('Digite um ano de nascimento: '))
    idade = date.today().year - ano
    if idade < 18:
        nfoi += 1
    else:
        foi += 1
print('{} pessoas atingiram a maior idade.'.format(foi))
print('{} pessoas n�o atingiram a maior idade.'.format(nfoi))