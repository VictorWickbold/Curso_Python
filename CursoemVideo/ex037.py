n = int(input('Digite um número inteiro: '))
e = int(input('\nEscolha uma das opções para representar o número {}:\n1. Binário\n2. Octal\n3. Hexadecimal\nDigite a opção: '.format(n)))

if e == 1:
    print('\nO número {} em BINÁRIO é: {}'.format(n, bin(n)[2:]))
elif e == 2:
    print('\nO número {} em Octal é: {}'.format(n, oct(n)[2:]))
elif e == 3 :
    print('\nO número {} em Hexadecimal é: {}'.format(n, hex(n)[2:]))
else:
    print('\nNenhuma opção válida selecionada!')
    exit()