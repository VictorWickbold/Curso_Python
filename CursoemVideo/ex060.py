n = int(input('Digite um número: '))
f = n
r = 1
print(f'Calculando {n}!')
while f > 0:
    print(f'{f}', end = '')
    print(' x ' if f > 1 else ' = ', end = '')
    r *= f
    f -= 1
print(f'{r}')