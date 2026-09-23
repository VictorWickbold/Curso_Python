from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 10, tente adivinhar...')
print('-=-'*20)
r = 0
p = 0
c = randint(0,10)
print('SORTEANDO...\n')
sleep(2)
while r != c:
    print('-=-' * 10)
    r = int(input('Qual número eu pensei? : '))
    if c == r:
        print('\nVOCÊ GANHOU!')
    else:
        print('\nVocê PERDEU!, tente novamente'.format(c))
    p += 1
print(f'Você precisou de {p} palpites')
