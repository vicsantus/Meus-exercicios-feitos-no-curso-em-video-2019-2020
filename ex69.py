contdezoito = mans = womens = 0
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()
    while True:
        if sexo == 'M' or sexo == 'F':
            break
        else:
            sexo = str(input('Digite um sexo válido!')).upper().strip()
    if idade > 18:
        contdezoito += 1
    if sexo == 'M':
        mans += 1
    if sexo == 'F':
        if idade < 20:
            womens += 1
    cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    while True:
        if cont == 'S' or cont == 'N':
            break
        else:
            cont = str(input('Opção inválida!')).upper().strip()
    if cont == 'N':
        break
print(f'Existe(m) {contdezoito} pessoa(s) menor(es) de 18 anos.')
print(f'Foi(ram) cadastrado(s) {mans} homen(s).')
print(f'Foi(ram) cadastrada(s) {womens} mulhere(s) menor(es) de 20 anos.')