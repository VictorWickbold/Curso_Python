from random import randint
from time import sleep
from operator import itemgetter

jogos = { 'Jogador1': randint(1, 6),
          'Jogador2': randint(1, 6),
          'Jogador3': randint(1, 6),
          'Jogador4': randint(1, 6)}

ranking = []

print('-'*40)
print('Valores Sorteados:')
for k, v in jogos.items():
    print(f'{k} tirou {v} no dado.')

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)

print('-'*40)
for k, v in enumerate(ranking):
    print(f'{k+1}º lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)