from random import randint

print('-=' * 10)
print('PAR OU ÍMPAR')
print('-=' * 10)

c = 0

while True:
    pc = randint(0, 11)
    jogador = int(input('Escolha um valor: '))
    pi = str(input('Você que par ou ímpar? [P/I] ')).strip().upper()
    total = jogador + pc

    if total % 2 == 0:
        if pi == 'P':
            print('\nVOCÊ GANHOU\n')
            c +=1
        else:
            print('\nVOCÊ PERDEU\n')
            break
    else:
        if pi == 'I':
            print('\nVOCÊ GANHOU\n')
            c += 1
        else:
            print('\nVOCÊ PERDEU\n')
            break
    print('-=' * 20)
    print('Vamos jogar novamente...')
    print('-=' * 20)
print('-=' * 20)
print(f'Você ganhou {c} vezes seguidas')
print('-=' * 20)
