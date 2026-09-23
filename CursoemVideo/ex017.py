from math import hypot
o = float(input('Digite o valor do cateto oposto: '))
a = float(input('Digite o valor do cateto adjacente: '))
h = hypot(o, a)
print('='*45)
print('O valor da hipotenusa é: {:.2f}'.format(h))
print('='*45)