#2. Escreva um programa que preencha uma matriz 4 x 6 com números inteiros,
#calcule e mostre na tela:
#a) A quantidade de números que estão no intervalo entre 10 e 30
#b) A soma dos números maiores que 10 e pares
#c) A soma dos números que estão na quarta coluna da matriz
#d) A média dos números da matriz que estão na terceira linha

from random import randint

mat=[]

for i in range(4):
    linha=[]
    for j in range(6):
        linha.append(randint(1,20))
    mat.append(linha)

for i in range(4):
    print(mat[i])

soma=soma2=qtd=soma3=0
for i in range(4):
    for j in range(6):
        if mat[i][j] >= 10 and mat[i][j] <=30:
            qtd+=1

        if mat[i][j] > 10 and mat[i][j] % 2 == 0:
            soma+=mat[i][j]

        if j == 3:
            soma2+=mat[i][j]

        if i == 2:
            soma3+=mat[i][j]

media=soma3/6

print('A quantidade de números que estão no intervalo entre 10 e 30: ',qtd)
print('A soma dos números maiores que 10 e pares: ',soma)
print('A soma dos números que estão na quarta coluna da matriz: ',soma2)
print('A média dos números da matriz que estão na terceira linha: ',media)
