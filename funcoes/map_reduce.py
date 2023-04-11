from functools import reduce


# for i in range(len(notas)):
#    notas[i] = notas[i] +1.5
# print(notas)

def somar_nota(delta):
    def somar(nota):
        return nota + delta
    return somar


notas = [6.4, 7.2, 5.8, 8.4]

notas_finais_1 = list(map(somar_nota(1.5), notas))
print(notas_finais_1)


def somar2(a, b):
    return a+b


total = reduce(somar2, notas, 0)
print(total)
