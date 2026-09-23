peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Está ABAIXO do peso')
elif 18.5 <= imc < 25:
    print('Está com o peso IDEAL')
elif 25 <= imc < 30:
    print('Está com SOBREPESO')
elif 30 <= imc < 40:
    print('Está com OBESIDADE')
else:
    print('Está com OBESIDADE MÓRBIDA')