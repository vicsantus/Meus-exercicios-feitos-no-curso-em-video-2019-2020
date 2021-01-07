cgeral = 0
while cgeral < 1:
    print('===JOGO DA FORCA===')
    pala1 = str(input('Digite uma palavra, ou frase: '))
    dica = str(input('Digite uma dica: '))
    t1 = int(input('Quantas tentativas você quer dar? '))
    tentativas = 0
    print('\n' * 130)
    pala1 = pala1.strip()
    pala1 = pala1.lower()
    print('A palavra/frase tem {} letra(s).'.format(len(pala1.replace(' ', ''))))
    pala2 = ''
    p2 = pala1
    char = ' '
    while pala2 != pala1:
        print('A dica é "{}".'.format(dica.capitalize()))
        letra = str(input('Digite uma letra: '))
        letra = letra.lower()
        if letra.strip() == pala1:
            pala2 = pala1
            break
        tentativas += 1
        if tentativas == t1:
            pala2 = pala1
            break
        letra = letra[0]
        char = char + letra
        if letra in pala1:
            contc = len(char)
            while contc > 0:
                contc -= 1
                p2 = p2.replace(char[contc], '')
            cont = len(p2)
            palac = pala1
            while cont > 0:
                cont -= 1
                palac = palac.replace(p2[cont], '_')
            print('\n{}.\n'.format(palac.upper()))
            pala2 = palac
        else:
            print('Não tem a letra "{}" na palavra/frase.'.format(letra.upper()))
        print('\nLetras já chutadas "{}".\n'.format(char.upper().replace(' ', '')))
        print('Você tem {} tentativas restantes.\n\n'.format(t1-tentativas))
    print('Parabêns, a palavra/frase é "{}".'.format(pala2.upper()))
    teste = str(input('\n\nDeseja jogar novamente? (Digite "S" ou "N"): '))
    antbabaca = 0
    while antbabaca < 1:
        if teste.upper() == 'N':
            cgeral += 1
            antbabaca += 1
        elif teste.upper() == 'S':
            print('\n'*130)
            antbabaca += 1
        else:
            teste = str(input('Escreve direito babaca! É "S" ou "N": '))