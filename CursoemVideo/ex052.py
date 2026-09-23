n = int(input('Digite um número: '))
v = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;33m', end=' ')
        v += 1
    else:
        print('\033[1;31m', end=' ')
    print(f'{c}', end=' ')

print(f'\n\033[mO número {n} foi divisível {v} vezes')

if v == 2:
    print('Ele é primo')
else:
    print('Ele não é primo')
