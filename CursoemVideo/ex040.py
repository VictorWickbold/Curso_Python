n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('\nSua média foi: {:.1f}\n'.format(m))
if m < 5:
    print('Infelizmete você reprovou, estude mais!')
elif 5 <= m <= 6.9:
    print('Você tem uma segunda chance na RECUPERAÇÃO, estude!')
else:
    print('Parabéns você foi APROVADO!!!')