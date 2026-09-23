maior18 = homens = mulher20 = 0
continua = 'S'
while continua == 'S':
    print('=' * 20)
    print('CADASTRE UMA PESSOA')
    print('=' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if idade > 18:
            maior18 += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulher20 += 1
    continua = ' '
    print('-=' * 25)
    while continua not in 'SN':

        continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('-=' * 25)
    if continua == 'N':
        break

print(f'Foram cadastradas {maior18} pessoas com mais de 18 anos')
print(f'Foram cadastrados {homens} homens')
print(f'Foram cadastradas {mulher20} mulheres com menos de 20 anos')
print('-=' * 25)