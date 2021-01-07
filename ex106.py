def PyHelp(ajuda=True):
    while True:
        print('\033[1;30;42m^'*27)
        print('  SISTEMA DE AJUDA PyHELP  ')
        print('^'*27)
        print('\033[m')
        ajuda = str(input('\033[30mFunção ou bibliotéca > \033[m')).lower().strip()
        if ajuda == 'fim':
            print('\033[1;30;41mATÉ LOGO')
            print('\033[m')
            break
        print('\033[1;31m')
        help(ajuda)
        print('\033[m')


PyHelp()