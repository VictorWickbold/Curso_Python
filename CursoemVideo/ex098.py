from defs import titulo
from time import sleep


def contador(inicio, fim, passo):
    print('='*40)

    if passo < 0:
        passo *= -1

    if passo == 0:
        passo = 1

    print(f'Contando de {inicio} até {fim} pulando de {passo} em {passo}')

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(cont, end=' - ')
            cont += passo
            sleep(0.5)
    else:
        cont = inicio
        while cont >= fim:
            print(cont, end=' - ')
            cont -= passo
            sleep(0.5)
    print('FIM')
    print('='*40)


titulo('Contador automático')

contador(1, 10, 1)
contador(10, 0, 2)

titulo('Contador personalizado')

inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio, fim, passo)
