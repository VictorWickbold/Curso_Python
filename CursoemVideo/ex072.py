extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
n = -1
erro = ''
while n not in range(0, 21):
    n = int(input(f'{erro}Digite um número entre 0 e 20: '))
    if n < 0 or n > 20:
        erro = '\nNúmero inválido, tente novamente.\n'
    else:
        print(f'O número {n} por extenso é: {extenso[n]}')
