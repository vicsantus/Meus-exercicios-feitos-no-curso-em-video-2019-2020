num = 0
soma = 0
cont = 0
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número (digite 999 para sair): '))
print('Foram contabilizados {} números, e a soma total deles é igual a {}.'.format(cont-1, soma))