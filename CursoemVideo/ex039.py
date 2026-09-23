from datetime import date

ano = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade < 18:
    print('Você deverá se alistar daqui {} anos'.format(18-(idade)))
elif idade == 18:
    print('Você deve se alistar este ano')
else:
    print('Você deveria ter se alistado a {} anos atras'.format(idade-18))