p = s = c = 0

while True:
    p = int(input('Digite um numero [999 para parar]: '))
    if p == 999:
        break
    else:
        s += p
    c += 1
print(f'A soma de todos os {c} números digitados é: {s}')
print('FIM DO PROGRAMA')