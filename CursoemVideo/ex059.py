n = me = s = mu = 0

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

while n != 5:

    print('-=-' * 10)
    n = int(input('''Escolha uma das opções:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos número
[ 5 ] Sair do programa

Sua opção: '''))
    print('\n')
    print('-=-' * 10)

    if n == 1:
        s = n1 + n2
        print(f'Resultado da soma : {s}')
    elif n == 2:
        mu = n1 * n2
        print(f'Resultado da multiplicação : {mu}')
    elif n == 3:
        if n1 > n2:
            me = n1
        else:
            me = n2
        print(f'O maior número é: {me}')
    elif n == 4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif n != 5:
        print('Opção inválida, digite novamente!')

print('Fim do programa')
print('-=-' * 10)
