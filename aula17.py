'''n = list()
qt = int(input('Quantos valores você quer adicionar?: '))
for q in range(0, qt):
    n.append(int(input('Digite um valor: ')))
for c, f in enumerate(n):
    print(f'Na posição {c+1}, chegay ao valor {f}!')
b = n[:]
b[2] = 99
print(n)
print(b)
g = []
g.append(n[:])
g.append(b[:])
print(g)
print('FIM!')'''
g = []
dados = []
for c in range(0, 5):
    dados.append(str(input('Digite o nome: ')).capitalize().strip())
    dados.append(int(input('Digite a idade: ')))
    g.append(dados[:])
    dados.clear()
print(g)