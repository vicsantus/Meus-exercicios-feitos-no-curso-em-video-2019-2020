def voto(a):
    from datetime import datetime
    anoatual = datetime.today().year
    idade = anoatual - a
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    elif 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


ano = int(input('Em que ano você nasceu?: '))
print(voto(ano))