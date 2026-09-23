def area(comp, larg):
    a = comp * larg
    print('-' * 60)
    print(f'A área de um terreno de {comp}m X {larg}m é de: {a}m²')
    print('-' * 60)


print('-' * 30)
print('Calculadora de área')
print('-' * 30)

comprimento = float(input('Comprimento (m): '))
largura = float(input('Largura (m): '))
area(comprimento, largura)
