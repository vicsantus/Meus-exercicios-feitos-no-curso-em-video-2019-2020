pares = []
impares = []
lista = []
while True:
    num = int(input('Digite um número (digite 0 para sair): '))
    if num == 0:
        break
    lista.append(num)
for c in range(0, len(lista)):
    if lista[c] % 2 == 0:
        pares.append(lista[c])
    else:
        impares.append(lista[c])
print(f'Os valores digitados foram {lista}.')
print(f'Os valores pares digitados foram {pares}.')
print(f'Os valores impares digitados foram {impares}.')