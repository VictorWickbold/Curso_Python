vel = float(input('Qual a velocidade do carro? : '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você ultrapassou o limite de velocidade de 80 km/h em {:.0f}km/h \nVocê foi multado em R${:.2f}'.format((vel-80), multa))
    print('Dirija com cuidado!')
else:
    print('Velocidade permitida, tenha um bom dia e dirija com segurança')