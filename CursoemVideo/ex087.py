matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma3 = maior2 = pares = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            soma3 += matriz[l][c]
        if l == 1 and matriz[l][c] > maior2:
            maior2 = matriz[l][c]


print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()


print('-=' * 30)
print(f'A soma dos valores pares digitados é: {pares}')
print(f'A soma da 3ª coluna é: {soma3}')
print(f'O maior valor da segunda linha é: {maior2}')