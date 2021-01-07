larg = float(input('Qual a largura da parede?  '))
alt = float(input('Qual a altura da parede? '))
area = larg * alt
print('Você vai precisar de {}L de tinta para pintar uma área de {}m².'.format(area/2, area))