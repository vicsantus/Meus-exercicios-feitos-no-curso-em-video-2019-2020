def Msg(msg):
    print('-' * (len(msg) + 8))
    print('   ', msg, '   ')
    print('-' * (len(msg) + 8))


Msg(str(input('Escreva uma mensagem:\n')).title().strip())