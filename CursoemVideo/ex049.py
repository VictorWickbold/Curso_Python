n = int(input('Digite um número: '))
print('-='*10)
print(f'A tabuada de {n} é:')
print('-='*10)
for c in range(1, 11):
    print(f'{n} x {c} = {n*c}')
print('-='*10)