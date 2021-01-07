frase = str(input('Digite uma frase aleatória, igual a sua mãe: '))
fr = frase.strip()
fr = fr.lower()
if 'a' in fr:
    print('A frase tem {} letras "A".'.format(fr.count('a')))
    print('A letra "A" aparece a primeira vez na posição {}.'.format(fr.find('a')))
    print('A letra "A" aparece por ultima vez na posição {}.'.format(fr.rfind('a')))
else:
    print('Não tem letra "A" na frase.')