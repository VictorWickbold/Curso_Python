def voto(ano):
    from datetime import date

    idade = date.today().year - ano

    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif idade >= 16 and idade < 18 or idade > 69:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


print(voto(int(input('Digite o ano de nascimento: '))))
