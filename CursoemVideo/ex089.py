escola = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    escola.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('=='*15)
print(f'{"Nº":<4}{"NOME":<15}{"MÉDIA":>10}')
print('--'*15)
for i, l in enumerate(escola):
    print(f'{i+1:<4}{l[0]:<15}{l[2]:>10.1f}')
