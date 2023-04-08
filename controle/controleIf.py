nota = float(input('Informe a nota do aluno: '))
comportado =True if input('Comportado? (y/n) ') == 'y' else False
if nota >= 9 and comportado:  # Bloco é por dentação do tab O que esta na mesma endentacao esta no mesmo bloco
    print('Parabéns :P')
    print('Quadro de Honra')
elif nota >= 7:
    print('Aprovado')
elif nota >= 5:
    print('recuperação')
else:
    print('Reprovado')

print(nota) #Fora do bloco

