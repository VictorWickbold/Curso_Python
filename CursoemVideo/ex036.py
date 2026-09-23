casa = float(input('Digite o valor da casa: R$ '))
sal = float(input('Digite o valor do seu salário: R$ '))
mes = int(input('Digite quantos anos deseja pagar: '))*12
pres = casa / mes
print('\nPara pegar uma casa de R$ {:.2f} em {:.0f} anos, a prestação será de R$ {:.2f} em {:.0f} meses\n'.format(casa, (mes/12), pres, mes))
if (sal/10 * 3) >= pres:
    print('Seu empréstimo foi APROVADO!')
else:
    print('Infelizmente seu empréstimo foi NEGADO!')