for i in range(3):
    print(f'Primeiro for 0 ao 2: {i}')
for i in range(1,6):
    print(f'for 1 ao 5: {i}')
for i in range(0,11,2):
    print(f'for de 2 em 2: {i}')
for i in range(20,0,-2):
    print(f'for regrecivo de 2 em 2: {i}')

nums = [2,4,6,8,10]

for n in nums:
    print(n,end=',')
print()
texto = 'Pyton é Massa'

for letra in texto:
    print(letra,end=' ')
print()

for n in {1,2,3,4}:
    print(n,end=',')
print()
produto= {
    'nome': 'caneta',
    'preco': 5.40,
    'desconto': 0.5
}
print('For Com dicionarios')
print('primeiro Exemplo')
for atrib in produto:
    print(atrib,'==>',produto[atrib ])
print('Segundo Exemplo')
for atrib,valor in produto.items():
    print(atrib,'==' , valor)
print('Terceiro Exemplo')
for valor in produto.values():
    print(valor,end=',')
print()
for ch in produto.keys():
    print(ch,end=',')
print()