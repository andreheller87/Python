#!python

# print('Ola Mundo!')

# import pacote.sub.arquivo

# from tipos import variavel,basicos
# from tipos import lista
# from tipos import tuplas
# from tipos import conjuntos
# from tipos import dicionario

# from operadores import aritmeticosEUnitarios
# from operadores import relacionaisEAtribuicao
# from operadores import ternario

# from controle import controleIf
# from controle import repeticaoFor
# from controle import repeticaoWhile

from funcoes import basicoFuncoes
from funcoes import map_reduce

basicoFuncoes.saudacao()
basicoFuncoes.saudacao(idade=30)
basicoFuncoes.saudacao('André')
basicoFuncoes.saudacao('André', 35)
x = basicoFuncoes.soma_e_mult(x=10, a=5, b=3)
print(x)

total = basicoFuncoes.soma(10, 25, 15, 36)

print(total)

resultado = basicoFuncoes.resultado_final(nome='Andre', nota=5)

print(resultado)

resultadoDaSoma = basicoFuncoes.operacao_aritmeticas(basicoFuncoes.soma2, 3, 5)
resultadoDaSub = basicoFuncoes.operacao_aritmeticas(basicoFuncoes.sub, 20, 5)

print(f'Resultado da soma: {resultadoDaSoma}')
print(f'Resultado da sub: {resultadoDaSub}')

lista = [5, 7.2, 5.8, 8.4]
total = map_reduce.reduce(map_reduce.somar2, lista, 0)

print(total)
