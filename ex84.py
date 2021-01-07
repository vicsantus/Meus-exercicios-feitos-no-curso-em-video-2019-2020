pessoas = []
dados = []
print('Digite 0 e de ENTER a qualquer momento para sair.')
while True:
    nome = str(input('Digite o nome: ')).capitalize().strip()
    if nome == '0':
        break
    peso = int(input('Digite o peso: '))
    if peso == 0:
        break
    dados.append(peso)
    dados.append(nome)
    pessoas.append(dados[:])
    dados.clear()
pessoas.sort()
print(f'Foram cadastradas {len(pessoas)} pessoas.')
pesados = pessoas[:]
pesados.sort(reverse=True)
pesados = pesados[0:3]
print(f'Os mais pesados foram ', end='')
for c, d in pesados:
    print(d, end=', ')
print('com ', end='')
for c, d in pesados:
    print(c, end='Kg, ')
print('respectivamente.')
leves = [pessoas[0], pessoas[1], pessoas[2]]
print(f'Os mais leves foram {leves}')