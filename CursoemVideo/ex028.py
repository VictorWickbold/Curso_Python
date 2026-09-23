from random import randint
from time import sleep
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5, tente adivinhar...')
print('-=-'*20)
c = randint(0,5)
print('SORTEANDO...\n')
sleep(2)
r = int(input('Qual número eu pensei? : '))
if c == r:
    print('\nVOCÊ GANHOU!')
else:
    print('\nVocê PERDEU!, pensei no número {}'.format(c))
