frase = str(input('Digite uma frase aleat�ria, igual a sua m�e: '))
fr = frase.strip()
fr = fr.lower()
if 'a' in fr:
    print('A frase tem {} letras "A".'.format(fr.count('a')))
    print('A letra "A" aparece a primeira vez na posi��o {}.'.format(fr.find('a')))
    print('A letra "A" aparece por ultima vez na posi��o {}.'.format(fr.rfind('a')))
else:
    print('N�o tem letra "A" na frase.')