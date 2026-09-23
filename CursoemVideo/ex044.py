normal = float(input('Digite o valor do produto: '))
cond = int(input('''Escolha a forma de pagamento:
[ 1 ] Dinheiro / Cheque
[ 2 ] Cartão à vista
[ 3 ] 2X no Cartão
[ 4 ] 3x ou mais no Cartão
Opção: '''))
if cond == 1:
    val = normal - (normal * 0.10)
    dj = 'com 10 % de desconto'
elif cond == 2:
    val = normal - (normal * 0.05)
    dj = 'com 5 % de desconto'
elif cond == 3:
    val = normal
    dj = ''
elif cond == 4:
    val = normal + (normal * 0.20)
    dj = 'com 20 % de juros'
else:
    print('Essa forma de pagamento é invalida')

print('O valor da sua compra ficou R$ {:.2f} {}'.format(val, dj))
