notacem = notacinq = notavinte = notadez = notaum = notacinco = 0
valor = int(input('Digite o valor a ser sacado: '))
v = valor
while True:
    if valor >= 100:
        notacem += 1
        valor -= 100
    elif valor >= 50:
        notacinq += 1
        valor -= 50
    elif valor >= 20:
        notavinte += 1
        valor -= 20
    elif valor >= 10:
        notadez += 1
        valor -= 10
    elif valor >= 5:
        notacinco += 1
        valor -= 5
    elif valor >= 1:
        notaum += 1
        valor -= 1
    elif valor == 0:
        break
print(f'O valor de R${v:.2f} é igual a:')
print(f'''{notacem} notas de 100, 
{notacinq} notas de 50
{notavinte} notas de 20
{notadez} notas de 10
{notacinco} notas de 5
{notaum} notas de 1 real.''')