num = 0
soma = 0
cont = 0
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um n�mero (digite 999 para sair): '))
print('Foram contabilizados {} n�meros, e a soma total deles � igual a {}.'.format(cont-1, soma))