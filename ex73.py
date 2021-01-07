time = ('qwer', 'wert', 'erty', 'rtyu', 'tyui', 'yuio', 'uiop', 'asdf', 'Chapecoense', 'dfgh', 'fghj', 'ghjk', 'hjkl', 'jklç',
        'zxcv', 'xcvb', 'cvbn', 'vbnm', 'bnm,', 'nm,.')
for c in range(0, 5):
    print(f'{c + 1}º colocado: {time[c]}')
print('\n')
for c in range(0, 4):
    print(f'Piores colocados: {time[c - 4]}')
print('\n', sorted(time))
n = time.index('Chapecoense')
print(f'O time Chapecoense está na posição {n+1}.')