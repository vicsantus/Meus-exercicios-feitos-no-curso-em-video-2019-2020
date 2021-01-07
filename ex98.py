from time import sleep
def Contagem(ini, fim, passo):
    while True:
        if ini < fim:
            if passo == 0:
                passo = 1
            print(f'Contagem de {ini} até {fim} de {passo} em {passo}.')
            for c in range(ini-1, fim, passo):
                sleep(0.5)
                print(c + 1, end=' ')
            print('FIM!')
            break
        elif ini > fim:
            if passo > 0:
                passo = passo - (passo * 2)
            if passo == 0:
                passo = -1
            print(f'Contagem de {ini} até {fim} de {passo - (passo * 2)} em {passo - (passo * 2)}.')
            for c in range(ini, fim-1, passo):
                sleep(0.5)
                print(c, end=' ')
            print('FIM!')
            break
        else:
            print('Opção de inválida!')


print('-='*30)
Contagem(1, 10, 1)
print('-='*30)
Contagem(10, 0, 2)
print('-='*30)
print('Agora é a sua vez de personalizar a contagem!')
Contagem(int(input('Início: ')),
         int(input('Fim: ')),
         int(input('Passo: ')))