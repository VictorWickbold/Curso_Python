t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 1
mais = 10
total = 0

while mais != 0:
    total += mais
    while c <= total:
        print(f'{t}', end = ' -> ')
        t += r
        c += 1
    print('PAUSA')
    mais = int(input('Digite a quantidade de termos adicionais: '))

print(f'Foram apresentados {c - 1} termos da PA')
print('FIM DO PROGRAMA')