city = str(input('Digite o nome da cidade: '))
c = city.lower().split()
if 'santo' in c[0:][0]:
    print('Sua cidade come�a com a palavra "Santo".')
else:
    print('Sua cidade n�o come�a com a palavra "Santo".')