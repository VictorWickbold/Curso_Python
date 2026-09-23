sal = float(input('Digite o valor do salario: '))
if sal <= 1250:
    val = sal + (sal * 15 / 100)
else:
    val = sal + (sal * 10 / 100)
print('Seu novo salário será: R$ {:.2f}'.format(val))
