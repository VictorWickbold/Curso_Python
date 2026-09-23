l = float(input('Qual a largura da parede em metros: '))
a = float(input('Qual a altura da parede em metros: '))
ar = l*a
lt = ar/2
print('='*45)
print('A área da parede é: {:.2f} \nVocê vai precisar de {:.2f} litros de tinta'.format(ar, lt))
print('='*45)