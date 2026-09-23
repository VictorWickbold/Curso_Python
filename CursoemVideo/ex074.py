from random import randint

aleatorios = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'Os números sorteados foram: {aleatorios}')
print(f'O menor número sorteado foi {min(aleatorios)} e o maior foi {max(aleatorios)}')