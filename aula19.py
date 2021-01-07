pessoas = {'nome': 'Pedro',
           'idade': 26,
           'sexo': 'M'}
pessoas['feiura'] = 100
for c, f in pessoas.items():
    print(f'{c.capitalize()}: {f}')