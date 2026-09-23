total = maismil = baratop = 0
baraton = ' '

while True:
    print('=' * 8)
    print('COMPRAS')
    print('=' * 8)
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total += preco

    if baratop == 0:
        baraton = nome
        baratop = preco
    if preco < baratop:
        baraton = nome
        baratop = preco
    if preco > 1000:
        maismil += 1

    continua = ' '
    print('-=' * 25)
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-=' * 25)
    if continua == 'N':
        break

print(f'Total: R${total:.2f}')
print(f'Produtos que custam mais de R$1000.00: R$ {maismil}')
print(f'O produto mais barato foi: ({baraton}), que custa: R$ {baratop:.2f}')
