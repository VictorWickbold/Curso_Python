sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
        sexo = str(input('Sexo invalido, digite novamente\nSexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))