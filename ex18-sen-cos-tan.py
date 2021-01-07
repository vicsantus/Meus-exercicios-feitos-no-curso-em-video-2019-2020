from math import sin, cos, tan, radians
from fractions import Fraction

num = int(input('Digite um ângulo: '))
print('Para um ângulo de {3}° graus valor do seno é {0}, do conseno é {1} e da tangente '
      'é {2}.'.format(Fraction(sin(radians(num))).limit_denominator(), Fraction(cos(radians(num))).limit_denominator(),
                     Fraction(tan(radians(num))).limit_denominator(), num))
print('Em numeral o valor de seno é {:.3f}, do coseno é {:.3f},'
      ' e da tangente é {:.3f}'.format(sin(radians(num)), cos(radians(num)), tan(radians(num))))