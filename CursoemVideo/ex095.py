jogador = dict()
gols = list()
time = list()

while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    part = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))

    for c in range(1, part+1):
        gols.append(int(input(f'Quantos gols na partida {c}? ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())

    while True:
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if continua in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continua == 'N':
        break

print('=='*30)

print('cod ', end='')
for c in jogador.keys():
    print(f'{c:<15} ', end='')

print()
print('-'*41)

for k, v in enumerate(time):
    print(f'{k:^3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()

print('-'*41)

while True:
    print('==' * 30)
    busca = int(input('Quer buscar os dados de qual jogador? [999 para parar]: '))
    print('==' * 30)
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe um jogador com o código {busca}')
    else:
        print(f'Dados do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols.')