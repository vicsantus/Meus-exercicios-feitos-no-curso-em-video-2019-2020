'''s = ''.upper()
while s != 'F' and s != 'M':
    s = str(input('Digite o sexo [M/F]: ')).upper()
    if s != 'F' and s != 'M':
        print('Valor inv�lido!')
        print('Somente os valores "F" e "M" s�o aceitos.')
''' #meu programa
# programa do professor abaixo
sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo inv�lido. Digite novamente: ')).strip().upper()[0]
print('Sexo confirmado!')