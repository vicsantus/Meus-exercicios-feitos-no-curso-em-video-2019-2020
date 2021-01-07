palabras = ('ferdinando', 'estetoscopio', 'fumo', 'de', 'rolo', 'cheirador', 'corcova', 'aspecto', 'pirocoptero')
for c in palabras:
    print(f'\nNa palavra {c.upper()} temos', end=' ')
    for letra in c:
        print(letra, end=' ') if (letra.lower() in 'aeiou') else None