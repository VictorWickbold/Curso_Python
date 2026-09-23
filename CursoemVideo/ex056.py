
m = 0
hvelho = ''
maior = 0
menor = 0

for p in range(1, 5):
    print(f'===== {p} PESSOA =====')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).strip()

    m += idade

    if p == 1 and sexo in 'Mm':
        maior = idade
        hvelho = nome
    if sexo in 'Mm' and idade > maior:
        hvelho = nome
        maior = idade
    elif sexo in 'Ff' and idade < 20:
        menor += 1

print(f'\nA média das idades é: {m/4}')
print(f'O homem mais velho tem {maior} e é o {hvelho}')
print(f'Temos {menor} mulheres com menos de 20 anos')