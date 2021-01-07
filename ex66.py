cont = soma = 0
while True:
    num = int(input('Digite um número (aperte 999 pra parar): '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} valores, e a soma total é {soma}.')