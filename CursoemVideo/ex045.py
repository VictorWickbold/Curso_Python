from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

c = randint(0, 2)

j = int(input('''
Escolha uma opção para jogar:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Sua opção: '''))

if 2 >= j >= 0:

    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-=' * 16)
    print('O computador escolheu {}'.format(itens[c]))
    print('O jogador escolheu {}'.format(itens[j]))
    print('-=' * 16)

    if c == j:
        print('Empate')
    elif c == 0:
        if j == 1:
            print('Jogador venceu')
        else:
            print('Jogador perdeu')
    elif c == 1:
        if j == 0:
            print('Jogador perdeu')
        else:
            print('Jogador venceu')
    else:
        if j == 0:
            print('Jogador venceu')
        else:
            print('Jogador perdeu')

else:
    print('Escolha inválida')