times = ('Palmeiras', 'Flamengo', 'Athletico-PR', 'Fluminense', 'Bahia', 'Cruzeiro',
         'Coritiba', 'Atlético-MG', 'Bragantino', 'Corinthians', 'São Paulo', 'Botafogo',
         'EC Vitória', 'Santos', 'Grêmio', 'Mirassol', 'Vasco da Gama', 'Internacional', 'Remo', 'Chapecoense')

pos = 0

print('=' * 20)
print('TABELA BRASILEIRÃO')
print('=' * 20)

while pos in range(0, len(times)):
    print(f'{pos +1}º - {times[pos]}')
    pos += 1

print('=' * 20)
print(f'Os primeiros cinco são: {times[:5]}')
print('=' * 20)
print(f'Os últimos quatro são: {times[-4:]}')
print('=' * 20)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('=' * 20)
print(f'O chapecoence está na posição: {times.index("Chapecoense")+1}º')