lista = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    continua = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continua == 'N':
        break

print('-' * 30)
print(f'Voce digitou {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print(f'O número 5 esta presente na lista')
else:
    print('O valor 5 não foi encontrado na lista')
