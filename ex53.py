frase = str(input('Digite uma frase: ')).lower().strip()
palavras = frase.split()
junto = ''.join(palavras)
inv = ''
for l in range(len(junto) - 1, -1, -1):
    inv += junto[l]
frase = frase.replace(' ', '')
if inv == frase:
    print('"{}" invertido � igual a "{}".'.format(frase, inv))
    print('A frase � pal�ndrome!')
else:
    print('"{}" invertido � igual a "{}".'.format(frase, inv))
    print('A frase n�o � palindrome')