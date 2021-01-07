tidade = 0
sexo = ''
midade = 0
mnome = ''
vinte = 0
for r in range(0, 4):
    print('\n---{}ª pessoa---'.format(r+1))
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    rep = 0
    while rep < 1:
        sexo = str(input('Digite o sexo (M/F): ')).upper()
        if sexo != 'M' and sexo != 'F':
            print('Digite um sexo válido!')
        else:
            rep += 1
    tidade += idade
    if sexo == 'M':
        if idade > midade:
            midade = idade
            mnome = nome
    elif sexo == 'F':
        if idade < 20:
            vinte += 1
media = tidade / 4
print('A média de idades é de {:.2f} anos.'.format(media))
print('O home mais velho tem {} anos, e o seu nome é {}.'.format(midade, mnome.title()))
print('Existem um total de {} mulher(es) com menos de 20 anos.'.format(vinte))