expr = str(input('Digite uma expressão: '))
paren = list()
for simb in expr:
    if simb == '(':
        paren.append('(')
    elif simb == ')':
        if len(paren) > 0:
            paren.pop()
        else:
            paren.append(')')
            break

if len(paren) == 0:
    print('Sua expressão está com os parenteses corretos.')
else:
    print('Sua expressão NÂO está com os parenteses corretos.')