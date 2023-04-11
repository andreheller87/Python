#x = 0
#while x != -1:
    #x=float(input('Informe Um numero ou -1 para sair: '))
#print('Fim')

total =0
qtde = 0
nota = 0
media =0
while nota != -1:
    nota = float(input('Informe a nota ou -1 para sair: '))
    if nota != -1:
        qtde+=1
        total += nota
if qtde != 0:
    media = total / qtde
print(f'Meidia da turma é : {media}')

