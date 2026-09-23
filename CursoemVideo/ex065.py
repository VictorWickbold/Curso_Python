n = m = maior = menor = s = 0
c = 'S'
cont = 0
while c in 'Ss':
    n = int(input('Digite um numero: '))
    c = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cont == 0:
        maior = menor = n
    if n > maior:
        maior = n
    else:
        menor = n
    cont += 1
    s += n
m = s / cont
print(f'\nA media de todos os números digitados é: {m}')
print(f'O maior digitado foi {maior} e o menor foi {menor}')
print('\nFIM DO PROGRAMA')