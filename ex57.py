'''s = ''.upper()
while s != 'F' and s != 'M':
    s = str(input('Digite o sexo [M/F]: ')).upper()
    if s != 'F' and s != 'M':
        print('Valor inválido!')
        print('Somente os valores "F" e "M" são aceitos.')
''' #meu programa
# programa do professor abaixo
sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido. Digite novamente: ')).strip().upper()[0]
print('Sexo confirmado!')