termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a raz�o: '))
pa = termo
dec = 11
while dec != 0:
    pa = pa + razao
    print(pa, end='    ')
    if dec == 1:
        dec = int(input('\nVoc� quer encontrar mais quantos termos? (digite 0 para sair): '))
        dec += 1
    dec -= 1