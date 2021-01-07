from datetime import date
ano = int(input('Digite o ano que voc� nasceu: '))
idade = date.today().year - ano
if idade < 18:
    prazo = 18 - idade
    print('Sua idade � de {} ano(s). Voc� ainda vai se alistar daqui '
          'a {} ano(s), em {}.'.format(idade, prazo, date.today().year + prazo))
elif idade == 18:
    print('Voc� completa ou j� completou 18 anos esse ano. Hora de se alistar!')
else:
    prazo = idade - 18
    print('Sua idade � de {} anos. Voc� se alistou, ou deveria ter '
          'se alistado a {} ano(s), em {}.'.format(idade, prazo, date.today().year - prazo))