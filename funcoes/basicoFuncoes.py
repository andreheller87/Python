def saudacao(nome='', idade=20):
    print(f'Bom Dia {nome}!\n Você nem parece ter {idade} anos')


def soma_e_mult(a, b, x):
    return a+b*x


def soma(*nums):
    total = 0
    for n in nums:
        total += n
    return total


def resultado_final(**kwargs):
    status = 'APROVADO(A)' if kwargs['nota'] >= 7 else 'REPROVADO(A)'
    return f'{kwargs["nome"]} foi {status}'


def soma2(a, b):
    return a+b


def sub(a, b):
    return a-b


def operacao_aritmeticas(fn, a, b):
    return fn(a, b)
