city = str(input('Digite o nome da cidade: '))
c = city.lower().split()
if 'santo' in c[0:][0]:
    print('Sua cidade começa com a palavra "Santo".')
else:
    print('Sua cidade não começa com a palavra "Santo".')