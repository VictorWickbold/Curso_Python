def ficha(nome, gols):
    if gols.isnumeric() == False:
        gols = 0
    if nome == '':
        nome = '<desconhecido>'

    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

print(ficha(input('Nome do jogador: '), input('Número de gols: ')))