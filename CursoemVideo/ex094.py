turma = list()
pessoa = dict()
soma = media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    turma.append(pessoa.copy())

    while True:
        continua = str(input('Quer continuar? [S/N] ')).upper()[0]
        if continua in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continua == 'N':
        break

media = soma / len(turma)

print('-='*30)

print(f'Ao todo temos {len(turma)} pessoas cadastradas.')

print(f'A média de idade é: {media:5.2f} anos.')

print('As mulheres cadastradas foram: /', end='')
for c in turma:
    if c['sexo'] == 'F':
        print(f'{c["nome"]} ', end='/ ')
print('\nLista das pessoas com idade acima da média: /', end='')
for c in turma:
    if c['idade'] >= media:
        print(f'{c["nome"]} ', end='/ ')