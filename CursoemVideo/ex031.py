dis = float(input('Digite a distância da viagem: '))
if dis <= 200:
    v = dis * 0.50
else:
    v = dis * 0.45
print('Você deverá pagar R$ {:.2f}'.format(v))