from datetime import date

ano = date.today().year - int(input('Digite o ano de nascimento: '))
print('Idade: ',ano)
if ano <= 9:
    print('O atleta é MIRIM')
elif ano <= 14:
    print('O atleta é INFANTIL')
elif ano <= 19:
    print('O atleta é JUNIOR')
elif ano <= 20:
    print('O atleta é SENIOR')
else:
    print('O atleta é MASTER')