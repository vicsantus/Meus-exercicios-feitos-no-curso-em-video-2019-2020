def Area_terreno(larg: float, compri: float):
    area = larg * compri
    print(f'A �rea de um terreno {larg} x {compri} � de {area:.1f}m�')


print('  Controle de Terrenos')
print('-'*25)
Area_terreno(
    float(input('LARGURA (m): ')),
    float(input('COMPRIMENTO (m): '))
)