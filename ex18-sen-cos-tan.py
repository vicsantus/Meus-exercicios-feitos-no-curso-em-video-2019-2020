from math import sin, cos, tan, radians
from fractions import Fraction

num = int(input('Digite um �ngulo: '))
print('Para um �ngulo de {3}� graus valor do seno � {0}, do conseno � {1} e da tangente '
      '� {2}.'.format(Fraction(sin(radians(num))).limit_denominator(), Fraction(cos(radians(num))).limit_denominator(),
                     Fraction(tan(radians(num))).limit_denominator(), num))
print('Em numeral o valor de seno � {:.3f}, do coseno � {:.3f},'
      ' e da tangente � {:.3f}'.format(sin(radians(num)), cos(radians(num)), tan(radians(num))))