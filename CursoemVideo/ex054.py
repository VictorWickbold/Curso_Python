import datetime

p = 1
atual = datetime.date.today().year
maior = 0
menor = 0

for c in range(0, 7):
    ano = int(input(f'Digite o ano de nascimento da {p}ª pessoa: '))
    p += 1
    if (atual - ano) >= 21:
        maior += 1
    else:
        menor += 1
print(f'\nTemos {maior} pessoas maior de idade e {menor} pessoas menor de idade')

