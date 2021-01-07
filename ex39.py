from datetime import date
ano = int(input('Digite o ano que você nasceu: '))
idade = date.today().year - ano
if idade < 18:
    prazo = 18 - idade
    print('Sua idade é de {} ano(s). Você ainda vai se alistar daqui '
          'a {} ano(s), em {}.'.format(idade, prazo, date.today().year + prazo))
elif idade == 18:
    print('Você completa ou já completou 18 anos esse ano. Hora de se alistar!')
else:
    prazo = idade - 18
    print('Sua idade é de {} anos. Você se alistou, ou deveria ter '
          'se alistado a {} ano(s), em {}.'.format(idade, prazo, date.today().year - prazo))