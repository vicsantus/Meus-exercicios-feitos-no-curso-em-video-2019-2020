cont = soma = 0
while True:
    num = int(input('Digite um n�mero (aperte 999 pra parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} valores, e a soma total � {soma}.')