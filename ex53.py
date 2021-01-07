frase = str(input('Digite uma frase: ')).lower().strip()
palavras = frase.split()
junto = ''.join(palavras)
inv = ''
for l in range(len(junto) - 1, -1, -1):
    inv += junto[l]
frase = frase.replace(' ', '')
if inv == frase:
    print('"{}" invertido é igual a "{}".'.format(frase, inv))
    print('A frase é palíndrome!')
else:
    print('"{}" invertido é igual a "{}".'.format(frase, inv))
    print('A frase não é palindrome')