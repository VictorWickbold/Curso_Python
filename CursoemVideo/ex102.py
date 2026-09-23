def fatorial(n=1, show=False):
    """
        ==> Calcula o fatorial do número desejado.
    :param n: O número a ser calculado.
    :param show: (Opcional) Mostra ou não a conta feita.
    :return: O valor do fatorian do númro (n)
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c

        if show:
            print(c,end='')

            if c > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')

    return f


help(fatorial)

print(fatorial())
print(fatorial(5, True))
print(fatorial(5))

#print(fatorial(int(input('Digite um númeor para calcularmos seu fatorial: ')), str(input('Deseja mostrar a conta, se sim digite True'))))