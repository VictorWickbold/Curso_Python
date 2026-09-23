a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
if a < (b + c) and b < (c + a) and c < (b + a):
    print('Estes segmentos podem formar um triângulo')
else:
    print('Estes segmentos NÃO podem formar um triângulo')