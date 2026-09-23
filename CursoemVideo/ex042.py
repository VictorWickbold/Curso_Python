a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
if a < (b + c) and b < (c + a) and c < (b + a):
    print('Estes segmentos podem formar um triângulo')
    if a == b == c:
        print('Este triângulo é EQUILÁTERO')
    elif a != b != c and a != c:
        print('Este é um triângulo ESCALENO')
    else:
        print('Este é um triângulo ISÓSCELES')
else:
    print('Estes segmentos NÃO podem formar um triângulo')