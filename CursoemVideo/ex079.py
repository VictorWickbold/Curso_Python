continua = 'S'
num = list()

while continua == 'S':
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar...')

    print('-'*30)
    continua  = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-' * 30)
num.sort()
print(f'Voce digitou os valores: {num}')
