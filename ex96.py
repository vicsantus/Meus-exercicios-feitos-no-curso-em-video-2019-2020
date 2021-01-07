def Area_terreno(larg: float, compri: float):
    area = larg * compri
    print(f'A área de um terreno {larg} x {compri} é de {area:.1f}m²')


print('  Controle de Terrenos')
print('-'*25)
Area_terreno(
    float(input('LARGURA (m): ')),
    float(input('COMPRIMENTO (m): '))
)