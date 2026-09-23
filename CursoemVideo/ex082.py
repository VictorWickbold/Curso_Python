lista = list()
pares = list()
impares = list()

while True:
    lista.append(int(input('Digite um valor: ')))
    continua = str(input('Quer continuar? [S/N] ')).upper()[0]
    if continua == 'N':
        break

for p, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print(f'Números digitados: {lista}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')