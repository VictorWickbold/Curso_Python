valor = int(input('Qual valor você quer sacar: R$'))

cinquenta = vinte = dez = um = 0

while True:
    if valor >= 50:
        cinquenta += 1
        valor -= 50
    elif valor >= 20:
        vinte += 1
        valor -= 20
    elif valor >= 10:
        dez += 1
        valor -= 10
    elif valor >= 1:
        um += 1
        valor -= 1
    else:
        break
print('-='*20)
print(f'''Cédulas de R$50,00: {cinquenta}
Cédulas de R$20,00: {vinte}
Cédulas de R$10,00: {dez}
Cédulas de R$1,00: {um}''')
print('-='*20)